from flask import Flask, request, session, make_response, Response
from flask_sqlalchemy import SQLAlchemy
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from sqlalchemy import inspect

from langchain.chains.base import Chain
from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory

from redis import Redis
from rq import Queue

import json, time
from datetime import datetime
from uuid import uuid4
from pprint import pprint
from typing import List, Union, Optional
import asyncio

from ..run_redis_worker import query_job

def extract_memory(chain):
    return chain.memory.chat_memory.messages

def serialize_memory(chain: Chain) -> str :
    messages = extract_memory(chain)
    messages = messages_to_dict(messages)
    return json.dumps( messages )

def deserialize_memory(messages_str: Optional[str]) -> ConversationBufferMemory:
    if messages_str is None or len(messages_str) == 0:
        return ConversationBufferMemory(memory_key="chat_history", return_messages = True)
    messages = json.loads( messages_str )
    messages = messages_from_dict( messages )
    retrieved_chat_history = ChatMessageHistory(messages=messages)
    return ConversationBufferMemory(memory_key="chat_history", 
                                    chat_memory = retrieved_chat_history, 
                                    return_messages=True)

def get_conversation(sess, db, Conversation):
    return db.session.execute(
        db.Select(Conversation).where( Conversation.uid == sess.get('uid', '') ) 
    ).scalar_one_or_none()


def init_api(app: Flask, db: SQLAlchemy) -> None:

    gerty_queue = Queue(connection=Redis())

    with app.app_context():
        engine = db.engine
        inspector = inspect(engine)
        print(inspector.get_table_names())
        from ..db.langchain import Conversation

    
    @app.route('/api/')
    def index() -> str:
        convo: Conversation = db.session.execute(
            db.select(Conversation).where( Conversation.uid == session.get('uid', '') )
        ).scalar_one()
        convo.last_modified = datetime.utcnow()
        db.session.commit() 
        return session.get('uid', 'not-set')

    @app.route('/api/status')
    def status():
        return 'working!'
    
    @app.route('/api/login')
    def login() -> str:
        session['uid'] = str(uuid4())
        convo: Conversation = Conversation(
            uid = session['uid'],
            messages = "",
            last_modified = datetime.utcnow()
        )
        db.session.add(convo)
        db.session.commit()
        return 'ok'

    @app.route('/api/query', methods=['POST'])
    async def query():
        request_data = request.get_json()

        convo: Conversation = db.session.execute(
            db.select(Conversation).where( Conversation.uid == session.get('uid', '') )
        ).scalar_one()
        convo.last_modified = datetime.utcnow()

        job = gerty_queue.enqueue( 'run_redis_worker.query_job', args=(convo.messages, request_data['query']) )
        while not job.is_finished:
            await asyncio.sleep(1)
        result = job.return_value()

        convo.messages = result['messages']
        db.session.commit()

        return result['response']

    return 

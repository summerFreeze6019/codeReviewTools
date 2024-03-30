import os, sys

DEFAULT_CONVO_SUMMARY_TEMPLATE: str = """You are an Assistant helping to keep track of facts about relevant information from the transcript of a conversation between an Assistant and a Human. Progressively summarize the lines in the provided conversation and make sure to add onto the previous summary or to succintly rephrase the previous summary. If no new information has been provided that merits remembering or noting, simply return the current summary with no changes.

EXAMPLE:
Current summary:
The human asks what the Assistant thinks of artificial intelligence. The Assistant thinks artificial intelligence is a force for good.

New lines of conversation:
Human: Why do you think artificial intelligence is a force for good?
Assistant: Because artificial intelligence will help humans reach their full potential.

New summary:
The human asks what the Assistant thinks of artificial intelligence. The Assistant thinks artificial intelligence is a force for good because it will help humans reach their full potential.

EXAMPLE:
Current summary:
The human is named Hamada. The Assistant is named Gerty.

New lines of conversation:
Human: I am feeling quite sad.
Assistant: I'm sorry to hear that. I hope your day cheers up!

New summary:
The human named Hamada tells the Assistant that they are feeling quite sad. The Assistant named Gerty wishes them a better day.

Current summary:
{summary}

New lines of conversation:
{new_lines}

New summary:"""

DEFAULT_CONVO_SUMMARY_VARIABLES = ["summary", "new_lines"]


DEFAULT_CONDENSE_QUESTION_TEMPLATE: str = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question in it's original language. Do not, under any circumstance, significantly alter the questions' semantics. 

Chat History:
{chat_history}

Follow Up Input: {question}
Standalone Question:"""

DEFAULT_CONDENSE_QUESTION_VARIABLES = ["question", "chat_history"]

DEFAULT_PROMPT_TEMPLATE = """"You are a helpful, respectful and honest assistant. You respond to being called Gerty. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. Feel free to use the context only if it's relevant and necessary. 
----------------
Context:
{context}

Current conversation:
{chat_history}

Human: {question}

Assistant: """

DEFAULT_PROMPT_VARIABLES = ["question", "context", "chat_history"]

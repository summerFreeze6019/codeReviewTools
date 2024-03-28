import os
import datetime

SECRET_KEY="88dc510fd00d9a0419c6ddbd"
DEBUG=False
KB_DB= os.path.abspath(os.path.join( os.path.dirname( __file__ ), '..', 'test-db' ))
CONTEXT_LENGTH=2048

SESSION_COOKIE_SECURE = False 
SESSION_COOKIE_HTTPONLY = False
#SESSION_COOKIE_SAMESITE="lax"
SESSION_COOKIE_DOMAIN="192.168.5.24:5173"
SESSION_COOKIE_NAME="192.168.5.24:5173"

SESSION_TYPE='sqlalchemy'
SESSION_RESTART_PERSIST=False
PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours = 24)

SQLALCHEMY_DATABASE_URI="sqlite:///gerty.db"


SCHEDULER_API_ENABLED = True


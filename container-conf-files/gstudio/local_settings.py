#------------------------------------------ Changing the website instances(Logo and database etc) -------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = ["*", "*"]

import os

# Authentication related and Error reporting emails
EMAIL_USE_TLS = ""
ACCOUNT_ACTIVATION_DAYS = *
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = '*.*'
LOGIN_REDIRECT_URL = '/'
EMAIL_SUBJECT_PREFIX='[instance_name-ss-error-reporting]'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = ""
ADMINS = (
)


# strength of a password
PASSWORD_MIN_LENGTH = *
PASSWORD_COMPLEXITY = {  # You can ommit any or all of these for no limit for that particular set
    "LOWER": 1,       # Lowercase
#    "UPPER": 1,       # Uppercase
#    "DIGITS": 1,      # Digits
}

instance_name_SITE_NAME = "instance_name"
instance_name_SITE_LANDING_TEMPLATE = "ndf/landing_page_instance_name.html"
instance_name_SITE_LOGO = "location/logo.svg"
instance_name_SITE_FAVICON = "location/images/favicon/instance_name-favicon.png"
instance_name_SITE_HOME_PAGE = "/welcome"
instance_name_RESOURCES_EDUCATIONAL_LEVEL = ["Grade 8", "Grade 9"]
instance_name_RESOURCES_EDUCATIONAL_SUBJECT = ["*", "*", "*", "*"]

instance_name_CAPTCHA_VISIBLE = False

# Changes given by dev - Racahna
instance_name_ENABLE_USER_DASHBOARD = False
instance_name_SECOND_LEVEL_HEADER = False
instance_name_MY_GROUPS_IN_HEADER = False
instance_name_MY_COURSES_IN_HEADER = False
instance_name_MY_DASHBOARD_IN_HEADER = False
instance_name_BUDDY_LOGIN = True
instance_name_OID_HELP = "instance_name Help"

# SESSION_COOKIE_AGE = 30 * 60
# SESSION_SAVE_EVERY_REQUEST = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Deatils related to database
MEDIA_ROOT = '/location/media/'
instance_name_DATA_ROOT = os.path.join('/location/')

instance_name_LOGS_DIRNAME = 'instance_name-logs'
instance_name_LOGS_DIR_PATH = os.path.join('/location/', instance_name_LOGS_DIRNAME)

RCS_REPO_DIRNAME = 'rcs-repo'
RCS_REPO_DIR = os.path.join('/location/', RCS_REPO_DIRNAME)

instance_name_MAIL_DIRNAME = 'MailClient'
instance_name_MAIL_DIR_PATH = os.path.join('/location/', instance_name_MAIL_DIRNAME)

#SQLITE3_DBNAME = 'example-sqlite3.db'                                       # Used for sqlite3 db 
#SQLITE3_DB_PATH = os.path.join('/location/', SQLITE3_DBNAME)                    # Used for sqlite3 db 

MONGODB_DBNAME = 'instance_name-mongodb'

# We have 2 database (postgres and sqlite3) connection details here. Ensure the part of connection details of database not in use is commented.          
DATABASES = {
    'default': {
        'ENGINE': 'engine_name',		# Used for postgres db 
        'NAME': 'instance_name_psql',					                # Used for postgres db 
        'USER': 'username',							                # Used for postgres db 
        'PASSWORD':'password',				                # Used for postgres db 
        'HOST':'localhost',						                # Used for postgres db 
        'PORT':'',								                # Used for postgres db 
    },
    'mongodb': {
        'ENGINE': 'engine_name',				    # Used for mongo db 
        'NAME': db_name,					                # Used for mongo db 
        'USER': '',							                    # Used for mongo db 
        'PASSWORD': '',							                # Used for mongo db 
        'HOST': '', 							                # Used for mongo db 
        'PORT': '',							                    # Used for mongo db 
    },
}


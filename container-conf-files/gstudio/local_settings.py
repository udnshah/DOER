#------------------------------------------ Changing the website instances(Logo and database etc) -------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "*"]

import os

# Authentication related and Error reporting emails
EMAIL_USE_TLS = ""
ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'webmaster@clix.ss.org'
LOGIN_REDIRECT_URL = '/'
EMAIL_SUBJECT_PREFIX='[clix-ss-error-reporting]'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = ""
ADMINS = (
)


# strength of a password
PASSWORD_MIN_LENGTH = 6
PASSWORD_COMPLEXITY = {  # You can ommit any or all of these for no limit for that particular set
    "LOWER": 1,       # Lowercase
#    "UPPER": 1,       # Uppercase
#    "DIGITS": 1,      # Digits
}

GSTUDIO_SITE_NAME = "clix"
GSTUDIO_SITE_LANDING_TEMPLATE = "ndf/landing_page_clix.html"
GSTUDIO_SITE_LOGO = "/static/ndf/css/themes/clix/logo.svg"
GSTUDIO_SITE_FAVICON = "/static/ndf/images/favicon/clix-favicon.png"
GSTUDIO_SITE_HOME_PAGE = "/welcome"
GSTUDIO_RESOURCES_EDUCATIONAL_LEVEL = ["Grade 8", "Grade 9"]
GSTUDIO_RESOURCES_EDUCATIONAL_SUBJECT = ["English", "Mathematics", "Science", "Values"]

GSTUDIO_CAPTCHA_VISIBLE = False

# Changes given by dev - Racahna
GSTUDIO_ENABLE_USER_DASHBOARD = False
GSTUDIO_SECOND_LEVEL_HEADER = False
GSTUDIO_MY_GROUPS_IN_HEADER = False
GSTUDIO_MY_COURSES_IN_HEADER = False
GSTUDIO_MY_DASHBOARD_IN_HEADER = False
GSTUDIO_BUDDY_LOGIN = True
GSTUDIO_OID_HELP = "CLIx Help"

# SESSION_COOKIE_AGE = 30 * 60
# SESSION_SAVE_EVERY_REQUEST = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Deatils related to database
MEDIA_ROOT = '/data/media/'
GSTUDIO_DATA_ROOT = os.path.join('/data/')

GSTUDIO_LOGS_DIRNAME = 'gstudio-logs'
GSTUDIO_LOGS_DIR_PATH = os.path.join('/data/', GSTUDIO_LOGS_DIRNAME)

RCS_REPO_DIRNAME = 'rcs-repo'
RCS_REPO_DIR = os.path.join('/data/', RCS_REPO_DIRNAME)

GSTUDIO_MAIL_DIRNAME = 'MailClient'
GSTUDIO_MAIL_DIR_PATH = os.path.join('/data/', GSTUDIO_MAIL_DIRNAME)

#SQLITE3_DBNAME = 'example-sqlite3.db'                                       # Used for sqlite3 db 
#SQLITE3_DB_PATH = os.path.join('/data/', SQLITE3_DBNAME)                    # Used for sqlite3 db 

MONGODB_DBNAME = 'gstudio-mongodb'

# We have 2 database (postgres and sqlite3) connection details here. Ensure the part of connection details of database not in use is commented.          
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',		# Used for postgres db 
        'NAME': 'gstudio_psql',					                # Used for postgres db 
        'USER': 'glab',							                # Used for postgres db 
        'PASSWORD':'Gstudi02)1^',				                # Used for postgres db 
        'HOST':'localhost',						                # Used for postgres db 
        'PORT':'',								                # Used for postgres db 

#   'ENGINE': 'django.db.backends.sqlite3',				        # Used for sqlite3 db 
#   'NAME': SQLITE3_DB_PATH,		                            # Used for sqlite3 db          
    },
    'mongodb': {
        'ENGINE': 'django_mongokit.mongodb',				    # Used for mongo db 
        'NAME': MONGODB_DBNAME,					                # Used for mongo db 
        'USER': '',							                    # Used for mongo db 
        'PASSWORD': '',							                # Used for mongo db 
        'HOST': '', 							                # Used for mongo db 
        'PORT': '',							                    # Used for mongo db 
    },
}

#--------------------------------------------- Replication -----------------------------------------------------

# SMTP setting for sending mail (Using gmail SMTP server)
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'your_email_id'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'your_email_id' # mrunal4888@
#EMAIL_HOST_PASSWORD = 'your_password' 

# The following variables are for email id and password for the email account which will be used for receiving SYNCDATA mails
#SYNCDATA_FETCHING_EMAIL_ID = 'your_email_id'
#SYNCDATA_FETCHING_EMAIL_ID_PASSWORD = 'your_password'
#SYNCDATA_FETCHING_IMAP_SERVER_ADDRESS = 'imap_address_of_server'

# Mailing-list ID (ie to this id syncdata mails will be sent)
#SYNCDATA_SENDING_EMAIL_ID = (
#    'mailing_list_emil_id',
#) # Mailing list

#While sending syncdata mails the from field of the mail is set by this variable
#SYNCDATA_FROM_EMAIL_ID ='Display_name <your_email_id>' 
# sample:  'Gstudio <t.metastudio@gmail.com>'

# This is the duration (in secs) at which send_syncdata and fetch_syncdata scripts will be run
# SYNCDATA_DURATION = 60

#SIGNING KEY Pub. Fill the pub of the key with which to sign syncdata mails here
#SYNCDATA_KEY_PUB = 'gpg_public_key'


# ----------------------------------------------------------------------------
# following has to be at last
# just put every thing above it

try:
    from server_settings import *
    # print "Server settings applied"
except:
    # print "Default settings applied"
    pass

# ========= nothing to be added below this line ===========

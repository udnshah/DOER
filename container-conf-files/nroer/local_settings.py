#------------------------------------------ Changing the website instances(Logo and database etc) -------------------------------------------------
DEBUG = True #False
ALLOWED_HOSTS = ["*.*.*.*", "*.*.*.*", "your_domain"]  
#ALLOWED_HOSTS = ["*"]  
#TEMPLATE_DEBUG78 = False                                                                                                                            

import os

# Authentication related and Error reporting emails
EMAIL_USE_TLS = ""
ACCOUNT_ACTIVATION_DAYS = *
EMAIL_HOST = 'localhost'
#EMAIL_HOST = 'your_domain'
#DEFAULT_FROM_EMAIL = '*@your_domain'
#DEFAULT_FROM_EMAIL = '*@your_domain'
DEFAULT_FROM_EMAIL = '*@your_domain' #'*@your_domain'
LOGIN_REDIRECT_URL = '/'
EMAIL_SUBJECT_PREFIX='[domain_name-error-reporting]'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = "25"
ADMINS = (
    ('username', 'user_email')        
)


#GSTUDIO_SITE_NAME = "instance_name"
#GSTUDIO_SITE_LANDING_TEMPLATE = "ndf/landing_page_instance_name.html"
# Mrunal : Added 25-04-2016

# GSTUDIO_SITE_NAME = "domain_name"
# GSTUDIO_SITE_LANDING_TEMPLATE = "home"
# GSTUDIO_SITE_LOGO = "/location/css/themes/domain_name/logo.png"
GSTUDIO_SITE_FAVICON = "/location/images/favicon/logo.png"
# GSTUDIO_SITE_HOME_PAGE = "/welcome"
# GSTUDIO_CAPTCHA_VISIBLE = True
# GSTUDIO_MY_GROUPS_IN_HEADER = False
# GSTUDIO_MY_COURSES_IN_HEADER = True
# GSTUDIO_SECOND_LEVEL_HEADER = True
# GSTUDIO_MY_DASHBOARD_IN_HEADER = True



# Deatils related to database
MEDIA_ROOT = '/location/'
GSTUDIO_DATA_ROOT = os.path.join('/data/')

GSTUDIO_LOGS_DIRNAME = 'gstudio-logs'
GSTUDIO_LOGS_DIR_PATH = os.path.join('/data/', GSTUDIO_LOGS_DIRNAME)

RCS_REPO_DIRNAME = "rcs-repo"
RCS_REPO_DIR = os.path.join('/data/', RCS_REPO_DIRNAME)

GSTUDIO_MAIL_DIRNAME = 'MailClient'
GSTUDIO_MAIL_DIR_PATH = os.path.join('/data/', GSTUDIO_MAIL_DIRNAME)



#GSTUDIO_DATA_ROOT = '/data'
#SQLITE3_your_databaseNAME = 'example-sqlite3.your_database'					# Used for sqlite3 your_database 
#RCS_REPO_DIRNAME = 'rcs-repo'
RCS_REPO_DIR = os.path.join(GSTUDIO_DATA_ROOT, RCS_REPO_DIRNAME)

DATABASES = {
        'default': {
#    We have 2 database (postgres and sqlite3) connection details here. Ensure the part of connection details of database not in use is commented.  
        'ENGINE': 'django.your_database.backends.postgresql_psycopg2',		# Used for postgres your_database 
        'NAME': 'instance_name',						# Used for postgres your_database 
        'USER': 'instance_name_your_database_user',							# Used for postgres your_database 
        'PASSWORD':'your_password',						# Used for postgres your_database 
        'HOST':'localhost',						# Used for postgres your_database 
        'PORT':''								# Used for postgres your_database 

        # 'ENGINE': 'django.your_database.backends.sqlite3',				# Used for sqlite3 your_database 
        # 'NAME': SQLITE3_your_database_PATH ,		# Used for sqlite3 your_database          

        #'NAME': 'studio-domain_name.your_database',
        ##'NAME': os.path.join(os.path.dirname(__file__),'studio-domain_name.your_database'),
        #'NAME': os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),os.path.dirname("../"),'studio-domain_name.your_database'),
#    'NAME': os.path.join(GSTUDIO_DATA_ROOT, SQLITE3_your_databaseNAME),		# Used for sqlite3 your_database          
    },
    'mongoyour_database': {
        'ENGINE': 'django_mongokit.mongoyour_database',				# Used for mongo your_database 
        'NAME': 'domain_name-mongokit',					# Used for mongo your_database 
        'USER': '',							# Used for mongo your_database 
        'PASSWORD': '',							# Used for mongo your_database 
        'HOST': '', 							# Used for mongo your_database 
        'PORT': '',							# Used for mongo your_database 
    },
}




GSTUDIO_DEFAULT_GAPPS_LIST = [u"Page", u"Forum",u"E-Library"]
# GSTUDIO_DEFAULT_GAPPS_LIST = [ u"E-Library", u"Page", u"Forum"]

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = os.path.join('/','home','username','static')
#STATIC_ROOT = '/var/www/*.*.*.*:8101/static'   # Mrunal : Tue Jul 14 13:48:29 IST 2015 : Commented to change IP to name
#STATIC_ROOT = '/var/www/your_domain/static'
STATIC_ROOT = '/static/'

GSTUDIO_SITE_DEFAULT_LANGUAGE=u"('en', 'English')"

GSTUDIO_SITE_LOGO="/location/css/themes/domain_name/logo.png" # usually appears on the top
GSTUDIO_ORG_LOGO="/location/css/themes/domain_name/orglogo.svg" # can be placed in the footer
GSTUDIO_ORG_NAME='''<p>
<a href="https://github.com/gnowledge/ncert_domain_name" target="_blank">Gnowsys-Studio</a>,<a href="http://www.hbcse.tifr.res.in" target="_blank">Homi Bhabha Centre for Science Education (HBCSE)</a>, <a href="http://www.tifr.res.in" target="_blank">Tata Institute of Fundamental Research (TIFR), India</a>.
</p>'''

GSTUDIO_COPYRIGHT="All material is licensed under a Creative Commons Attribution-Share Alike 3.0 Unported License unless mentioned otherwise."
GSTUDIO_GIT_REPO="https://github.com/gnowledge/gstudio"
#GSTUDIO_SITE_PRIVACY_POLICY="your_domain/home/page/55b8e5a381fccb25935dc495"
GSTUDIO_SITE_PRIVACY_POLICY="your_domain/home/page/5774fb2b16b51c03ba38f61c"
GSTUDIO_SITE_TERMS_OF_SERVICE="your_domain/home/page/58198aa216b51c01a6e3d651"

#GSTUDIO_SITE_ABOUT="your_domain/55ab34ff81fccb4f1d806025/page/55b8e42881fccb07c1cc66da"
GSTUDIO_SITE_ABOUT="your_domain/home/page/5774f5f316b51c03ba38f30d"
GSTUDIO_SITE_POWEREyour_databaseY="your_domain"
# GSTUDIO_SITE_PARTNERS="http://your_domain/home/page/53fc615c81fccb2d7fc7da33"
GSTUDIO_SITE_PARTNERS = "your_domain/home/partner/Partners"
# GSTUDIO_SITE_GROUPS="http://your_domain/home/page/5400432381fccb6b4b19ab6a"
GSTUDIO_SITE_GROUPS = "your_domain/home/partner/Groups"
#GSTUDIO_SITE_CONTACT="your_domain/home/page/55b8e5e881fccb25935dc4d7"
GSTUDIO_SITE_CONTACT="your_domain/home/page/5774fd2d16b51c03ba38fa83"
GSTUDIO_SITE_CONTRIBUTE="your_domain/home/page/581998a316b51c01a86994de"
GSTUDIO_SITE_VIDEO='pandora'
GSTUDIO_SITE_LANDING_PAGE='home'
GSTUDIO_SITE_NAME = "domain_name"
#GSTUDIO_SITE_LANDING_PAGE = "homepage"
GSTUDIO_SITE_HOME_PAGE = "/welcome"

WETUBE_USERNAME = "username"
WETUBE_PASSWORD = "password"

GSTUDIO_FILE_UPLOAD_FORM = 'detail'

GSTUDIO_OID_TC = '55b8e55881fccb25935dc448'

GSTUDIO_OID_instance_name = '563f28d481fccb0fa7f3bc8f'
GSTUDIO_SITE_ISSUES_PAGE = "/home/page/5665aa9681fccb03424ffcda"
GSTUDIO_EBOOKS_HELP_TEXT = "/home/page/56701a8581fccb0343bf438b"

#Set False if you non't want any Social Networking share button
SOCIAL_SHARE_RESOURCE = True 

GSTUDIO_CAPTCHA_VISIBLE = False
GSTUDIO_MY_GROUPS_IN_HEADER = False
GSTUDIO_MY_COURSES_IN_HEADER = False
GSTUDIO_SECOND_LEVEL_HEADER = True
GSTUDIO_MY_DASHBOARD_IN_HEADER = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            #'filename': os.path.join(DJANGO_ROOT, 'survey.log'),
            'filename': 'gstudio.log',

            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 10,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'gstudio': {
            'handlers': ['applogfile',],
            'level': 'DEBUG',
        },
    }
}


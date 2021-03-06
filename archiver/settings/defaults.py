# QUEUE_NAME = 'celeryq'
CALLBACK_ADDRESS = [
    'http://192.168.111.111:7000/callback',
    'http://192.168.111.1:5000/api/v1/registration/finished/'
]

DEBUG = True
PORT = 7000
SENTRY_DSN = None
# Dont use celery just run everything syncronisly
CELERY_SYNC = False

#### FILE STORAGE OPTIONS ####
BACKEND = 's3'
CREATE_PARITIES = True
IGNORE_PARITIY_SIZE_LIMIT = False
#### FILE STORAGE LOCATIONS ####
FILES_DIR = 'Files/'
MANIFEST_DIR = 'Manifests/'
METADATA_DIR = 'File Metadata/'
DIRSTRUCT_DIR = 'Directory Structures/'
PARITY_DIR = 'Parities/'
### S3 Options ###
ACCESS_KEY = 'CHANGEME'
SECRET_KEY = 'CHANGEME'
BUCKET_NAME = 'CHANGEME'

### smartfile ###
smartfile_ACCESS_KEY = 'CHANGEME'
smartfile_SECRET_KEY = 'CHANGEME'

#### CELERY OPTIONS ####
BROKER_URL = 'amqp://archiver:archiver@192.168.111.112//'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_CHORD_PROPAGATES = False
CELERY_EAGER_PROPAGATES_EXCEPTIONS = CELERY_SYNC
CELERY_ALWAYS_EAGER = CELERY_SYNC
CELERY_RESULT_BACKEND = 'amqp'
CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.
CELERY_TRACK_STARTED = True
CELERY_IMPORTS = 'archiver.worker.tasks'
CELERY_REDIRECT_STDOUTS_LEVEL = 'INFO'
CELERY_ACKS_LATE = True
# Only process 5k jobs per hour
# This is to deal with API rate limiting
CELERY_DEFAULT_RATE_LIMIT = '5000/h'

#### CLONER OPTIONS ####
# Figshare
FIGSHARE_OAUTH_TOKENS = [
    'CLIENT ID',
    'CLIENT SECRET'
]

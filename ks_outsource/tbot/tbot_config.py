import django
from pathlib import Path
from django.conf import settings
from ks_outsource.my_set import DB_NAME, HOST_DB, PORT_DB, USER_DB, PASSWORD_DB

BASE_DIR = Path(__file__).resolve().parent.parent
settings.configure(
    DATABASES={
        'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER' : USER_DB,
        'PASSWORD' : PASSWORD_DB,
        'HOST' : HOST_DB,
        'PORT' : PORT_DB,
	}
    },
    INSTALLED_APPS=[
        'helpdesk',
    ]
)
django.setup()

# Now this script or any imported module can use any part of Django it needs.

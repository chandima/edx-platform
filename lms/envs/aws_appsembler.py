# aws_appsembler.py

from .aws import *
from .appsembler import *

import taxoman.settings
from taxoman_api.models import Facet


INSTALLED_APPS += ('appsembler', )
DEFAULT_TEMPLATE_ENGINE['OPTIONS']['context_processors'] += ('appsembler.context_processors.intercom',)

SEARCH_SKIP_ENROLLMENT_START_DATE_FILTERING = True

#enable course visibility feature flags
COURSE_CATALOG_VISIBILITY_PERMISSION = 'see_in_catalog'
COURSE_ABOUT_VISIBILITY_PERMISSION = 'see_about_page'

COURSE_DISCOVERY_FILTERS = ["org", "language", "modes"]

if FEATURES.get('ENABLE_TAXOMAN', False):
    # Maybe we want to include taxoman and taxoman_api in INSTALLED_APPS here?
    # But we'll need to fix the django_startup.py sequence issue first

    WEBPACK_LOADER['TAXOMAN_APP'] = {
        'BUNDLE_DIR_NAME': taxoman.settings.bundle_dir_name,
        'STATS_FILE': taxoman.settings.stats_file,
    }
    COURSE_DISCOVERY_FILTERS += list(Facet.objects.all().values_list('slug', flat=True))

# SENTRY
SENTRY_DSN = AUTH_TOKENS.get('SENTRY_DSN', False)

if SENTRY_DSN:

    # Set your DSN value
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
    }

    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)


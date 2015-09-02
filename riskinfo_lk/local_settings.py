# -*- coding: utf-8 -*-

import os
import settings

DEBUG = TEMPLATE_DEBUG = True

DEBUG_STATIC = False

REGISTRATION_OPEN = False

SITENAME = "RiskInfo"


LANGUAGES = (
    ('en', 'English'),
    ('si', 'Sinhala'),
    ('ta', 'Tamil'),
)

LANGUAGE_CODE = 'si'

EXTRA_LANG_INFO = {
    'si': {
        'bidi': False,
        'code': 'si',
        'name': 'Sinhala',
        'name_local': u'සිංහල', #unicode codepoints here
    },
    'ta': {
        'bidi': False,
        'code': 'ta',
        'name': 'Tamil',
        'name_local': u'Tamil', #unicode codepoints here
    },
}

# Location of translation files
LOCALE_PATHS = (
    os.path.join(settings.GEONODE_ROOT,"locale"),
    os.path.join(settings.LOCAL_ROOT,"locale"),
)

print LOCALE_PATHS

# Activate the Documents application
DOCUMENTS_APP = True
ALLOWED_DOCUMENT_TYPES = [
    'doc', 'docx','gif', 'jpg', 'jpeg', 'ods', 'odt', 'pdf', 'png', 'ppt', 
    'rar', 'tif', 'tiff', 'txt', 'xls', 'xlsx', 'xml', 'zip', 
]
MAX_DOCUMENT_SIZE = 20 # MB

#Monkey patch to add custom languages not provided by Django
#import django.conf.locale
#LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
#django.conf.locale.LANG_INFO = LANG_INFO

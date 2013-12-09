# -*- coding: utf-8 -*-

DEBUG = TEMPLATE_DEBUG = True

DEBUG_STATIC = False

REGISTRATION_OPEN = False

SITENAME = "RiskInfo"

LANGUAGES = (
    ('en', 'English'),
    ('si', 'Sinhala'),
)

EXTRA_LANG_INFO = {
    'si': {
        'bidi': False,
        'code': 'si',
        'name': 'Sinhala',
        'name_local': u'සිංහල', #unicode codepoints here
    },
}

# Activate the Documents application
DOCUMENTS_APP = True
ALLOWED_DOCUMENT_TYPES = [
    'doc', 'docx','gif', 'jpg', 'jpeg', 'ods', 'odt', 'pdf', 'png', 'ppt', 
    'rar', 'tif', 'tiff', 'txt', 'xls', 'xlsx', 'xml', 'zip', 
]
MAX_DOCUMENT_SIZE = 20 # MB

LOCALE_PATHS = (
    "/home/dmc/geonode_production/geonode/locale",
    "/home/dmc/riskinfo_lk2/riskinfo_lk/riskinfo_lk/locale",
    )

#Monkey patch to add custom languages not provided by Django
import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
django.conf.locale.LANG_INFO = LANG_INFO

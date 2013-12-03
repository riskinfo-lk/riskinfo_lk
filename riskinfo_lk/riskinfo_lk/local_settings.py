# -*- coding: utf-8 -*-

DEBUG = TEMPLATE_DEBUG = True

DEBUG_STATIC = False

#SITENAME = 'GeoNode'

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

# Monkey patch to add custom languages not provided by Django
import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
django.conf.locale.LANG_INFO = LANG_INFO

LOCKDOWN_GEONODE = True

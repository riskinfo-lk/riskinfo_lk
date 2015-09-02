# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import geonode
from geonode.settings import *
#
# General Django development settings
#
SITEURL = "www.riskinfo.lk"
# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
GEONODE_ROOT = os.path.abspath(os.path.dirname(geonode.__file__))

print GEONODE_ROOT

WSGI_APPLICATION = "riskinfo_lk.wsgi.application"

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'riskinfo_lk.urls'

# Load more settings from a file called local_settings.py if it exists

LOCKDOWN_GEONODE = False 

# Add additional paths (as regular expressions) that don't require authentication.
AUTH_EXEMPT_URLS = ()

if LOCKDOWN_GEONODE:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('geonode.security.middleware.LoginRequiredMiddleware',)

try:
    from local_settings import *
except ImportError:
    pass

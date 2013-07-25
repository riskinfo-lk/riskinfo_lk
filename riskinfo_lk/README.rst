Riskinfo_Lk
========================

Installation for development set-up
-----------------------------

Create a new virtualenv for riskinfo_lk, install GeoNode and setup your project::

    $ mkvirtualenv riskinfo_lk
    $ pip install Django
    $ django-admin.py startproject riskin_lk --template=https://github.com/GeoNode/geonode-project/archive/master.zip -epy,rst 
    $ pip install -e riskinfo_lk

To install the latest from GeoNode's master branch use the following command::

    $ pip install -e git+https://github.com/GeoNode/geonode.git#egg=geonode --upgrade

.. note:: You should NOT use the name geonode for your project as it will conflict with the default geonode package name.

Usage
-----

Setup your GeoNode for usage. Download a geoserver.war to use and start the development server::

    $ cd my_geonode
    $ paver setup # downloads geoserver
    $ paver start 

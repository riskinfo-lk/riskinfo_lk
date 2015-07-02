Riskinfo_Lk
========================

Installation for development set-up
-----------------------------

Create a new virtualenv for riskinfo_lk, install GeoNode and setup your project::

    $ mkvirtualenv riskinfo_lk

To install the latest from GeoNode's master branch use the following command::

    $ pip install -e git+https://github.com/GeoNode/geonode.git#egg=geonode --upgrade

Usage
-----

Setup your GeoNode for usage. Download a geoserver.war to use and start the development server::

    $ git clone https://github.com/riskinfo-lk/riskinfo_lk2.git 
    $ cd riskinfo_lk2/riskinfo_lk
    $ paver setup # downloads geoserver
    $ paver start 

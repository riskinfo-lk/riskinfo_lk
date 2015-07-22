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

Setting up the vagrant box
--------------
	$ git clone https://github.com/vdeparday/riskinfo_lk2.git

Change the ip in the VagrantFile to a valid ip on the local network 
For production configuration

	$ vagrant up production

or

For development

	$ vagrant up dev

The basic box will be downloaded automatically and will be provisioned with GeoNode (see the bash script)

	$ vagrant ssh [dev|production]
	$ geonode createsuperuser

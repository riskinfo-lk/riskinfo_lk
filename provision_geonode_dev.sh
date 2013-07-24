#!/usr/bin/env bash

#which virtualenv > /dev/null &&
#{ echo "Already provisioned"; exit 0; }

sudo apt-get update
sudo apt-get install python python-pip
sudo pip install virtualenvwrapper
#echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc 
#echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
#source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv riskinfo_lk
sudo pip install Django
django-admin.py startproject riskinfo_lk --template=https://github.com/GeoNode/geonode-project/archive/master.zip -epy,rst

sudo apt-get install python-dev python-lxml gdal-bin
sudo apt-get install openjdk-7-jdk
sudo apt-get install build-essential libxml2-dev libxslt-dev

cd riskinfo_lk

paver setup # install geonode and downloads geoserver
#paver start -b 0.0.0.0:8000
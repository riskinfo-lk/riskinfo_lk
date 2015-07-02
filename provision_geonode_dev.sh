#!/usr/bin/env bash

which virtualenv > /dev/null &&
{ echo "Already provisioned"; exit 0; }

sudo apt-get update
sudo apt-get -y install python python-pip git zlib1g-dev openjdk-7-jdk python-dev python-lxml gdal-bin build-essential libxml2-dev libxslt-dev libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

sudo pip install virtualenvwrapper
sudo pip install GDAL==1.10.0
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv riskinfo_lk

git clone https://github.com/riskinfo-lk/riskinfo_lk2.git
cd riskinfo_lk2/riskinfo_lk/ 

pip install geonode==2.4b25 
paver setup # install geonode and downloads geoserver
paver start -b 0.0.0.0:8000

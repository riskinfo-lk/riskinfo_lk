#!/usr/bin/env bash

which virtualenv > /dev/null &&
{ echo "Already provisioned"; exit 0; }

sudo apt-get update
sudo apt-get install python python-pip git
sudo pip install virtualenvwrapper
#sudo apt-get install python-dev python-lxml gdal-bin
#sudo apt-get install openjdk-7-jdk
#sudo apt-get install build-essential libxml2-dev libxslt-dev

#echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc 
#echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
#source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv riskinfo_lk

git clone https://github.com/riskinfo-lk/riskinfo_lk2.git
cd riskinfo_lk2/riskinfo_lk/ 

paver setup # install geonode and downloads geoserver
paver start -b 0.0.0.0:8000

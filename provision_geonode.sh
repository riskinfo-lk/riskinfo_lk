#!/usr/bin/env bash

set -x

which geonode > /dev/null &&
{ echo "Geonode already installed."; exit 0; }

add-apt-repository ppa:geonode/testing
apt-get update
apt-get install -y geonode
geonode-updateip 192.168.33.10
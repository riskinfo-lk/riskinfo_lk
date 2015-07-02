#!/usr/bin/env bash

set -x

ifconfig eth1 192.168.100.52 netmask 255.255.255.0 up

which geonode > /dev/null &&
{ echo "Geonode already installed."; exit 0; }

apt-get install -y python-software-properties
add-apt-repository ppa:geonode/snapshots
apt-get update
apt-get dist-upgrade -y
apt-get install -y geonode
geonode-updateip www.riskinfo.lk

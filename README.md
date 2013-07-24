
Setting up the vagrant box
--------------
	git clone https://github.com/vdeparday/riskinfo_lk2.git

Change the ip in the VagrantFile to a valid ip on the local network 
For production configuration
	vagrant up production

or
For development
	vagrant up dev

The basic box will be downloaded automatically and will be provisioned with GeoNode (see the bash script)
	vagrant ssh
	geonode createsuperuser

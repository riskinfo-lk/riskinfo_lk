# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "preciseserver64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/precise/current/precise-server-cloudimg-vagrant-amd64-disk1.box"
  config.vm.provision :shell, :path => "provision_geonode.sh"

  Vagrant.configure("2") do |config|
   config.vm.network :private_network, ip: "192.168.100.52"
   config.vm.provider :virtualbox do |vb|
	   config.vm.customize [ "modifyvm", :id, "--name", "RiskInfo - GeoNode 2.0","--memory", 8192 ]
   end
  end

end

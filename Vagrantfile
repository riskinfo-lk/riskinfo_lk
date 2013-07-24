# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "preciseserver64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/precise/current/precise-server-cloudimg-vagrant-amd64-disk1.box"

  config.vm.define :production do |production|
  	config.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    production.vm.provision :shell, :path => "provision_geonode.sh"
    config.vm.provider :virtualbox do |vb|
        vb.customize [ "modifyvm", :id, "--name", "RiskInfo2","--memory", 8192 ]
  	end
  end

  config.vm.define :dev do |dev|
  	config.vm.network :private_network, ip: "192.168.50.4"
  	config.vm.provider :virtualbox do |vb|
       vb.customize [ "modifyvm", :id, "--name", "RiskInfo2 - dev ","--memory", 4096 ]
  	end
  end

end

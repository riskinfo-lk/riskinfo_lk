# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "preciseserver64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/precise/current/precise-server-cloudimg-vagrant-amd64-disk1.box"
  config.vm.provision :shell, :path => "provision_geonode.sh"
  config.vm.network :public_network, :bridge => 'eth0', :auto_config => false
  config.vm.provider :virtualbox do |vb|
    vb.customize [ "modifyvm", :id, "--name", "RiskInfo2","--memory", 8192 ]
  end
end

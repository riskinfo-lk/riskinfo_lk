# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "preciseserver64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/precise/current/precise-server-cloudimg-vagrant-amd64-disk1.box"
  config.vm.network :hostonly, "192.168.33.10"
  # config.vm.network :bridged
  config.vm.forward_port 80, 8000
  config.vm.forward_port 8080, 8080
  # config.vm.share_folder "v-data", "/vagrant_data", "../data"
  
  config.vm.provision :shell, :path => "provision_geonode.sh"
  Vagrant.configure("2") do |config|
  # ... (other config)
    config.vm.provider :virtualbox do |vb|
	  config.vm.customize [ "modifyvm", :id, "--name", "RiskInfo - GeoNode 2.0","--memory", 8192 ]
   end
  end

end

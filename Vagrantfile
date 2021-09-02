# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :
# Box / OS
VAGRANT_BOX = 'ubuntu/bionic64'
# Memorable name for your
VM_NAME = 'new-vm-vagrant'

# VM User — 'vagrant' by default
VM_USER = 'vagrant'

# Username on your Mac
MAC_USER = 'fabian.flores'

# Host folder to sync
HOST_PATH = '/Users/fabian.flores/Documents/odoo-docker-server/src'

# Where to sync to on Guest — 'vagrant' is the default user name
GUEST_PATH = '/home/vagrant/src'
VAGRANT_HOME = GUEST_PATH

# # VM Port — uncomment this to use NAT instead of DHCP
# VM_PORT = 8080
Vagrant.configure(2) do |config|

  # Vagrant box from Hashicorp
  config.vm.box = VAGRANT_BOX

  # Actual machine name
  config.vm.hostname = VM_NAME

  # Set VM name in Virtualbox
  config.vm.provider "virtualbox" do |v|
    v.name = VM_NAME
    v.memory = 8192
    v.cpus = 2
  end

  #DHCP — comment this out if planning on using NAT instead
  #config.vm.network "private_network", type: "dhcp"
  config.vm.network :forwarded_port, guest: 80, host: 80
  config.vm.network :forwarded_port, guest: 5432, host: 5433
  3

  # # Port forwarding — uncomment this to use NAT instead of DHCP
  # config.vm.network "forwarded_port", guest: 80, host: VM_PORT
  # Sync folder
  config.vm.synced_folder HOST_PATH, GUEST_PATH

  # Disable default Vagrant folder, use a unique path per project
  config.vm.synced_folder '.', '/home/'+VM_USER+'', disabled: true

  #Install package for your VM
  config.vm.provision "shell", inline: <<-SHELL
    apt update
    apt install -y git
    apt install -y apt-transport-https
    apt install -y build-essential
    apt install -y curl
    apt install -y gnupg-agent
    apt install -y software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    apt-key fingerprint 0EBFCD88
    add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
    apt-get update -y
    apt-get install -y docker-ce docker-ce-cli containerd.io
    curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
  SHELL
end

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  # config.vm.synced_folder ".", "/var/webapps/cactusproj/code",
  #   owner: "testuser_dev", group: "users"
  config.vm.box_check_update = false
  config.vm.network :private_network, ip: "172.16.0.39"
  config.ssh.insert_key=false
  config.vm.provider "virtualbox" do |v|
    v.memory = 512
    v.cpus = 2
    v.name = "PlayGround"
  end
end

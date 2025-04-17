from ipaddress import ip_network

net = ip_network('172.16.128.0/255.255.192.0') #'172.16.128.0/18 - 18 - кол-во '1'
print(net.network_address)  #Адрес сети
print(net.netmask)  #Маска сети
print(net.broadcast_address)    #Широковещательный адрес
print(net.num_addresses) #Кол-во адресов(адрес сети + широковещательный + узлы)
print(net.hosts()) #Узлы текущей узлы
from ipaddress import ip_network, ip_address

net = ip_network('11.92.135.56/255.224.0.0', False)

print(max(net.hosts()))
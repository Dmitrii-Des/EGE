from ipaddress import ip_network, ip_address

net = ip_network('98.81.154.195/255.252.0.0', False)

print(max(net.hosts()))
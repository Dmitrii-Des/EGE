from ipaddress import ip_network, ip_address

ip = ip_address('143.172.12.114')
ip_net = ip_address('143.172.8.0')

for mask in range(16, 25):
    net = ip_network(f'143.172.12.114/{mask}', False)
    if ip in net.hosts() and net.network_address == ip_net:
        print(net.netmask)
        break
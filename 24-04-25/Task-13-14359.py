from ipaddress import ip_address, ip_network

ip1 = ip_address('157.127.172.56')
ip2 = ip_address('157.127.191.78')

for mask in range(0, 31)[::-1]:
    print(f'Current mask = {mask}')
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if ip1 in net1.hosts() and ip2 in net2.hosts():
        if net1.network_address != net2.network_address:
            print(mask)
from ipaddress import ip_network, ip_address

ip_net = ip_address('218.48.192.0')
ip = ip_address('218.48.192.56')
cnt = 0

for mask in range(16, 25):
    net = ip_network(f'{ip_net}/{mask}', False)
    if net.num_addresses >= 502 and ip_net != net.broadcast_address and ip_net == net.network_address and\
            ip in net.hosts():   #ip_net != net.broadcast_addres необязательно, адрес сети не может быть широковещателем
        cnt += 1

print(cnt)
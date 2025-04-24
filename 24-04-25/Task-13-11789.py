from ipaddress import ip_network, ip_address

for mask in range(16, 25):
    ip = ip_address(f'99.8.254.232')
    net = ip_network(f'{ip}/{mask}', False)
    for i in net:
        i = f'{int(i):032b}'
        if not(i[:16].count('1') <= i[16:].count('1')):
                break
    else:
        print(net.netmask)


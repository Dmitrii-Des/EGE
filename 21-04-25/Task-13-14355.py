from ipaddress import ip_address, ip_network

for mask in range(16, 25):
    ip = ip_address('127.63.67.1')
    net = ip_network(f'{ip}/{mask}', False)
    if ip in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if not(i[:17].count('1') >= i[17:].count('1')):
                break
        else:
            print(net.netmask)
            break

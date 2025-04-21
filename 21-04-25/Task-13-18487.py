from ipaddress import ip_address, ip_network

for A in range(256):
    ip = ip_address(f'192.214.{A}.184')
    net = ip_network(f'{ip}/255.255.255.224', False)
    if ip in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if not(i.count('1') > 15):
                break
        else:
            print(A)
            break
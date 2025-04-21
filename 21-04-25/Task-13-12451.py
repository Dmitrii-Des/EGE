from ipaddress import ip_address, ip_network

cnt = 0

for A in range(256):
    ip = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip}/255.255.255.224', False)
    if ip in net.hosts():
        for i in net.hosts():
            i = f'{int(i):032b}'
            if not(i[16:24].count('0') > i[24:].count('0')):
                break
        else:
            cnt += 1

print(cnt)

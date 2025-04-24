from ipaddress import ip_network, ip_address

ip = ip_address('143.131.211.37')

for mask in range(8, 31)[::-1]:
    net = ip_network(f'{ip}/{mask}', False)
    cnt = 0
    if ip in net.hosts():
        for i in net:
            if f'{int(i):032b}'.count('1') == 10:
                cnt += 1
            if cnt > 15:
                break
        if cnt == 15:
            print(mask)



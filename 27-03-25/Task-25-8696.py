def f(num):
    divs = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            divs |= {num, num//i}
    if len(divs) < 2 == 0:
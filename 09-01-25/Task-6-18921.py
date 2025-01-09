from turtle import*
lt(90)
tracer(0)
m = 10
for i in range(13):
    fd(13 * m)
    rt(90)
    fd(5 * m)
up()
rt(90)
fd(7 * m)
lt(90)
fd(10 * m)
down()
for i in range(23):
    fd(8 * m)
    lt(90)
    fd(11 * m)
    lt(90)
up()
for x in range(-20, 40):
    for y in range(-20, 40):
        goto(x * m, y * m)
        dot(3, 'white')
update()
print(18*18+11*8-7*3)
done()

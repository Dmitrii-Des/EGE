from turtle import*
m = 10
screensize(1000, 1000)
lt(90)
tracer(0)
for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(1*m)
lt(90)
down()
for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)
up()
for x in range(-20, 50):
    for y in range(-50, 40):
        goto(x*m, y*m)
        dot(3, 'white')
print(21*2+15*2)


update()
done()
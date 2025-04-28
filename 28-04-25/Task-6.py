from turtle import*
tracer(0)
screensize(5000, 5000)
m = 10
rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
bk(40*m)
rt(45)
down()
for i in range(5):
    fd(20*m)
    lt(90)
up()
for x in range(-200, -160):
    for y in range(-240, -200):
        goto(x*m, y*m)
        dot(3, 'magenta')

update()
done()
print(202*202+20*20)
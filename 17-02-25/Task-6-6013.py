from turtle import*
tracer(0)
lt(90)
m = 10

for i in range(2):
    rt(120)
    fd(7 * m)
for i in range(2):
    rt(120)
    fd(7 * m)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'magenta')

update()
done()
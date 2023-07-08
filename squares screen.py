
import turtle

wind = turtle.Screen()
wind.setup(500, 500)
wind.bgcolor('black')

abo_grgr = turtle.Turtle()
abo_grgr.speed(0)
abo_grgr.color('#8B7D6B')
abo_grgr.penup()
abo_grgr.goto(0, 0)
abo_grgr.pendown()
abo_grgr.pensize(3)


running_fd = 5

# draw a square
for i in range(500):
    abo_grgr.right(90)
    abo_grgr.fd(running_fd)
    running_fd+=5
turtle.mainloop()
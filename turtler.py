from node import Node
from turtle import Turtle, Screen, mode, done

iterations = int(input('How many iterations should there be? '))
count = 2**(iterations + 1) - 1

s = Screen()
width = 1000
height = 600
s.setup(width, height)
t = Turtle()

nodes = []
nodes.append(Node())

mode('standard')
t.speed(10)
t.pensize(2)
t.degrees()
while count > 0:
    n = nodes.pop(0)
    nodes.append(Node(n, 1))
    nodes.append(Node(n, -1))
    t.penup()
    t.setpos(n.pos)
    t.pendown()
    t.setheading(n.angle)
    t.forward(n.length)
    count -= 1

done()
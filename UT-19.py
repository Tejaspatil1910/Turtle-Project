import turtle
from turtle import *
t = turtle.Turtle()
hideturtle()
speed(10)
bgcolor("white")

colors = ["red","yellow","black"]   #list in python

for i in colors:
	t.fillcolor(i)
	t.begin_fill()
	for j in range(3):
		t.fd(300)
		t.lt(90)
		t.fd(50)
		t.lt(90)
	t.end_fill()
	t.fd(300)
	t.rt(180)


turtle.done()

# germany flag
	




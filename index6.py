import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(-100,200)
t.pendown()
t.write("Made by Tejas",align="left",font=("Serif",28))
while True:
	t.forward(a)
	t.right(b)
	a += 3
	b += 1
	if b == 210:
		break
		t.hideturtle()
turtle.done()


# TEJAS SHAMRAO PATIL
# NMIMS SHIRPUR

import turtle

turtle.bgcolor('gray')
turtle.speed(10)
turtle.pensize(2)


t=turtle.Turtle()
move=1
for i in range(360):
	t.pendown()
	t.right(move)
	t.forward(50)
	t.right(30)
	t.forward(360)
	t.left(30)
	t.forward(30)
	t.penup()
	t.home()
	move=move+1

# Tejas Shamrao Patil
# NMIMS Shirpur
# follow for more vidoe's

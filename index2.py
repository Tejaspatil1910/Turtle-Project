import turtle

colors = ['red','blue','green','orange','pink','yellow']
t=turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
	t.pencolor(colors[i%6])
	t.width(i/100+1)
	t.forward(i)
	t.left(59)
turtle.exitonclick()


# Tejas Shamrao Patil
# NMIMS Shirpur
# Follow for more videos

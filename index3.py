


import turtle as t

import colorsys
t.color('white')
style = ('Couries',30,'italic')
t.write('Made by Tejas : ........................ ',font = style,align = 'center',move = True) 

t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
hue=0.0
t.hideturtle()

for i in range (1000):
	color = colorsys.hsv_to_rgb(hue,1,1)
	t.pencolor(color)
	t.circle(130)
	t.left(95)
	t.circle(80)
	hue += 0.005
t.exitonclick()

# TEJAS SHAMRAO PATIL
# NMIMS SHIRPUR





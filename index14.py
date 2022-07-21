from turtle import*
speed(20)
bgcolor('black')
clr = ('cyan','red','white','yellow','lime')
a=200
for i in range(200):
	color(clr[i%5])
	circle(a,90)
	lt(90)
	circle(a,90)
	lt(18)
	a-=1
# Tejas Shamrao Patil
# Nmims Shirpur
	




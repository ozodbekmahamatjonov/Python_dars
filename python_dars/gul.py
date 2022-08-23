from turtle import *
import random

def gul():
	for i in  range(300):

		bgcolor('black')
		color('yellow')
		speed(0)
		circle(190-i,90)
		left(90)
		circle(190-i,90)
		left(190)
		pensize(1)

gul()
hideturtle()
mainloop()

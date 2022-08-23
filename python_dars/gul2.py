from turtle import *
import random

def gul():
	for i in  range(300):

		bgcolor('black')
		color('green')
		speed(20)
		circle(190-i,90)
		left(90)
		circle(190-i,90)
		left(150)

gul()
hideturtle()
mainloop()
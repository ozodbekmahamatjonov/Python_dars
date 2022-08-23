import turtle 

turtle.bgcolor('black')

turtle.speed(20)
turtle.pensize(1)
turtle.pencolor('blue')

def drawcircle(radius):
	for i in range(10):
		turtle.circle(radius)
		radius=radius-4


def drawdesign():
	for i in range(250):
		drawcircle(150)
		turtle.right(700)

drawdesign()
turtle.done()
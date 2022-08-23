from tkinter import *
import random 

GAME_WIDTH = 500
GAME_HEIGHT = 600 
SPEED = 50 
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000'


class Snake:
	pass

class Food:
	def __init__self(self):
		x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
		y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

		self.coordinates = [x, y]

		canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def  next_turn():
	pass

def change_direction(newdirection):
	pass

def check_collisions():
	pass

def game_over():
	pass


window = Tk()
window.title('Sanke game')
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text='Score:{}'.format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH )
canvas.pack()
window.update()
window_width = window_width()
window_height = window_height()
#screen_width = window.winfo_screenwidth()
#screen_height = window.winfo_screenheight()

snake = Snake()
food = Food()

window.mainloop()



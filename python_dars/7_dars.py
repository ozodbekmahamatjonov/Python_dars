til = input('Tilni tanlang: uz/en ?')
if til == 'uz':
	print('Assalomu alaykum')
elif til == 'en':
	print('HELLO')
else:
	print('uz/en lardan birini tanlang')

from random import randint

a = randint(1, 10)
b = randint(1, 10)

c = int(input('{} + {} = '.format(a, b)))

if c == (a + b):
	print('Vapshey Xato!')
else:
	print('Vapshey Xato!')
from datetime import datetime
from tkinter import * 
oyna = Tk()
oyna.title('Dasturcha:)')
oyna.geometry('300x300')
natija = Label(text='result',)
natija.place(x=90, y=135, width=120, height=40)


yil = Entry()
yil.place(x=75, y=50, width=150, height=30)


def natija():
	word=entry.get()
	translator=translator(service_url=[translate.google.com])
	result=translator.translate(word)



tugma = Button(text='Translate', command=natija)
tugma.place(x=90, y=90, width=120, height=40)

oyna.mainloop()
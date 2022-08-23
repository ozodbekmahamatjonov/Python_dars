#son = 45
#print('son= ', son, type(son))
#
#print('sonlar= ',  sonlar, type(sonlar))

#sonlar = [45, 61, 27, -91, 84, 'python', 25, 86]
#print(len(sonlar))
#sonlar.append('PHP')
#print(sonlar)

import pygal
line_chart = pygal.Line()
line_chart.title = 'Statistika'
line_chart.x_labels = ['Fevral', 'Mart', 'Aprel', 'May']
line_chart.add('Facebook', [9.24, 13.7, 16.24, 18.07])
line_chart.render_in_browser()
line_chart.mainloop()
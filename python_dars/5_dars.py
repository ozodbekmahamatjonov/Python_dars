# ikki xil vaqt kiritiladi
# time1 = soat1, minut1, secund1
# time2 = soat2, minut2, secund2

soat1 = int(input('1-soat'))
minut1 = int(input('1-minut'))
secund1 = int(input('1-secund'))

# 1 soat 3600 secund, 1 minut 60 secund

soat2 = int(input('2-soat'))
minut2 = int(input('2-minut'))
secund2 = int(input('2-secund'))
secund = (soat2 - soat1) * 3600 + (minut2 - minut1) * 60 + (secund2 - secund1)
print('secund: {}'.format(secund))
summa = input('Summani kiriting: ')
if summa.isdigit() and int(summa) > 0 and int(summa) < 1000000000:
	print('Tashakkur')
else:
	print('Xatolik bor!')


ism = input('Ismingizni kiriting: ')
fam = input('Familyangizni kiriting: ')

if ism or fam:
	print('Tashakkur')
else:
	print('Ism yoki familyangizni kiriting')

 8 - Dastur 1 dan 10gacha bo`lgan son kiriting .bularni so`zlar orqali ifodalash

son = input('1 dan 30 gacha son kiriting: ')
if son.isdigit():
	son = int(son)
  	if son > 9 and son < 30:
  		qoldiq = son % 10
  		letter = ''
  		if son > 9 and son 20:
  			letter == 'o`n '
  		if son > 19 and son 30:
  			letter == 'yigirma '


		if qoldiq == 1:
			letter += 'bir'
		elif qoldiq == 2:
			letter += 'ikki'
		elif qoldiq == 3:
			letter += 'uch'
		elif qoldiq == 4:
			letter += 'to`rt'
		elif qoldiq == 5:
			letter += 'besh'
		elif qoldiq == 6:
			letter += 'olti'
		elif qoldiq == 7:
			letter += 'yetti'
		elif qoldiq == 8:
			letter += 'sakkiz'
		elif qoldiq == 9:
			letter += 'to`qqiz'

		print(letter)
	elif:
		print('1 dan 30 gacha son kiritish kerak.')

else:
	print('Son kiritish kerak!')

	


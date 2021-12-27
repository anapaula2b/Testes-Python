from datetime import date


AnoAtual = date.today().year

AnoNas = int(input('Ano: '))

idade = AnoAtual - AnoNas

if idade <= 9:
	print('Mirim')
elif 14 >= idade:
	print('Infantil')
elif 19 >= idade:
	print('Junior')
elif 25 >= idade:
	print('Senior')
else:
	print('Master')

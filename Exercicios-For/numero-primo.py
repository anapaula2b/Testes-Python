numero = int(input('Digite um numero: '))
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else: 
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')

print(f'\n\033[m numero {numero} foi divisivel {total} vezes')
if total == 2:
    print('e um numero primo!!')
else:
    print('Não é umnumero primo')
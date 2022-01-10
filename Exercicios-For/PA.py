inicio = int(input('Primeiro termo:  '))
intervalo = int(input('Razão:  '))
decimo = inicio + (10 - 1) * intervalo
for i in range(inicio, decimo + intervalo, intervalo):
    print(f'{i}', end = '-> ')
print('Pronto')
from datetime import date
maior = 0
menor = 0
for i in range(7):
    data = int(input('Digite o ano de nascimento? '))
    teste =  date.today().year - data
    if teste >= 18:
        print('Maior de idade')
        maior += 1
    else:
        print('Menor de Idade')
        menor += 1
print(f'{maior} maiores de idade e {menor} menores de idade')
num = []

for i in range(0, 6):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        num.append(numeros)
print(f'A soma é: {sum(num)}')

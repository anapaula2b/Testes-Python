letras = []

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alfabeto)):
    letras.append(alfabeto[i])


print(letras)

for i in range(len(letras)):
    for a in range(9999):
            print(f'Sequencia: {letras[i]}{a} ')

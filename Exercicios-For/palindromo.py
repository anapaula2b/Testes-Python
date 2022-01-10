frase = input('Digita ai: ')
palavras = frase.split()

juntar = ''.join(palavras)

inverso = ''

for letras in range(len(juntar)-1, -1, -1):
    inverso += juntar[letras]

print(inverso)
if inverso == juntar:
    print('PALINDRMO!!!!!')
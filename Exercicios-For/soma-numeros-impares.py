soma = 0
for i in range(1,501, 2):
        teste = i%3
        if teste == 0:
            soma = soma + i
print(soma)
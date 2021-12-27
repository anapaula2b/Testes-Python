nota = int(input('Digite uma nota '))
nota2 = int(input('Digite uma nota '))

media = (nota + nota2)/2

print(f'A media do aluno é {media}')
if media >= 7:
	print('Aprovado')
elif 7 > media >= 5:
	print('Recuperação')
elif media < 5:
	print('Reprovado')

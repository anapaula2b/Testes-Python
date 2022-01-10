from _typeshed import SupportsItemAccess


somaidade = 0
qnt = int(input('Quantas pessoas vão ser analisadas? '))

for i in range(qnt):
    print(f'--------- {i+1} pessoa ---------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    genero = input('Genero: ').strip()
    somaidade += idade 

mediaidade = somaidade/4


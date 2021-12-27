import random
from time import sleep

continuar = 1

opções = ['pedra', 'papel', 'tesoura']

print('''PEDRA, PAPEL E TESOURA
        0 - PEDRA 
        1 - PAPEL
        2 - TESOURA 
'''
)



while continuar == 1:
    escolhaJogador = int(input('Escolha sua opção '))

    jogador = opções[escolhaJogador]
    computador = random.choice(opções)

    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA!!')
    sleep(1)

    print('----------------------------')
    print(f'COMPUTADOR: {computador}')
    print(f'VOCE: {jogador}')
    print('----------------------------')

    if jogador == computador:
        print('EMPATE! ')
    elif jogador == opções[0] and computador == opções[1]:
        print('YOU WIN!')
    elif jogador == opções[1] and computador == opções[0]:
        print('VOCE PERDEU.')
    elif jogador == opções[2] and computador == opções[1]:
        print('YOU WIN!')
    elif jogador == opções[1] and computador == opções[2]:
        print('VOCE PERDEU.')
    elif jogador == opções[0] and computador == opções[2]:
        print('YOU WIN!')
    elif jogador == opções[2] and computador == opções[0]:
        print('VOCE PERDEU.')

    print('Para continuar jogando digite 1, para parar digite 0 ')
    continuar = int(input())
    
    if continuar == 0:
        print('GAME OVER')
        break
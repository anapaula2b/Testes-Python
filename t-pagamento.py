import math

valor = float(input('Qual o valor da sua compra? R$'))

print(''' Forma de pagamento 
1 - A vista 
2 - 2x cartão 
3 - 3x ou mais no cartão
''')
pagamento = int(input('Qual vai ser a forma de pagamento '))
if pagamento == 1:
    total = valor - (valor * 10/100)
    print(f'O valor da sua compra teve um desconto de 10% {total}')
elif pagamento == 2:
    print(f'Voce vai pagar 2 parcelas de R${valor/2}')
elif pagamento == 3:
    parcelas = int(input('Quantas parcelas? '))
    total = valor/parcelas +  (valor/parcelas * 5/100)
    print(f'Voce vai pagar {parcelas} parcelas de {total} com 5% de juros')
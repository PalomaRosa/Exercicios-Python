# Crie um programa que faça o computador jogar Jokenpô com você.
# Pedra quebra tesoura e vence. Porém perde para papel.
# Papel embrula a pedra e vence. Porém perde para tesoura.
# Tesoura corta o papel e vence. Porém perde para pedra.

from time import sleep
from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA \n''')
jogador = int(input('Sua opção: '))

if jogador > 2:
    print('\nJogada inválida, pois foi digitado uma opção não permitido! Opção digitada: {}. \n\nTente novamente!'.format(
        jogador))
else:
    sleep(2)
    print('\nJO')
    sleep(2)
    print('KEN')
    sleep(2)
    print('PO!!\n')
    print('-=-'*10)
    print('Computador jogou {} \nJogador jogou {}'.format(itens[computador], itens[jogador]))
    print('-=-'*10)
    #Computador vence
    if (itens[computador] == 'Pedra' and itens[jogador] == 'Tesoura') \
            or (itens[computador] == 'Papel' and itens[jogador] == 'Pedra') \
            or (itens[computador] == 'Tesoura' and itens[jogador] == 'Papel'):
        print('\nO computador venceu!')
    #Jogador vence
    elif (itens[computador] == 'Pedra' and itens[jogador] == 'Papel') \
            or (itens[computador] == 'Papel' and itens[jogador] == 'Tesoura') \
            or (itens[computador] == 'Tesoura' and itens[jogador] == 'Pedra'):
        print('\nO jogador venceu!')
    else:
        print('\nEMPATE!')

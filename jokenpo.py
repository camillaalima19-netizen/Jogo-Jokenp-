import time
from random import randint

print('VAMOS JOGAR JOKENPÔ!')
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print(''' Suas opções:
[0] PEDRA
[2] TESOURA
[5] PAPEL''')
jogo = int(input('Qual é a sua jogada?: '))
print('='*40)
time.sleep(1)
if computador == jogo:
    print('EMPATOU. Jogue de novo!')
elif computador == 0  and jogo == 5:
    print('você GANHOU!')
elif computador == 0 and jogo == 2:
    print('Você PERDEU!')
elif computador == 2 and jogo == 0:
    print('Você GANHOU')
elif computador == 2 and jogo == 5:
    print('você PERDEU!')
elif computador == 5 and jogo == 2:
    print('você GANHOU')
elif computador == 5 and jogo == 0:
    print('você PERDEU')
else:
    print('opção invalida')
print(' ')
print (' O computador escolheu: {}'.format(itens[computador]))
print(' Você escolheu: {}'.format(itens[jogo]))
























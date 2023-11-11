from random import randint
from time import sleep
from suporte import *

#programa principal
cabeçalho()
computador = randint(0, 10)
premio = ['Celular', 'Tênis', 'Pc Gamer']
sorteio = randint(0, 3)
ok = False

for contador in range(1, 5):
    print(f'Tentativa - {contador} ')
    jogador = verificação('Digite um numero (0 à 10):')
    sleep(0.8)
    if jogador == computador:
        print(f'PARABÉNS, Você ganhou ', end='')
        print(premio[sorteio])
        premio.remove(f'{premio[sorteio]}')
        if contador != 4:
            resp = str(input('Quer continuar [S/N]: ')).upper()[0]
            if resp in 'N':
                ok = True
    else:
        if computador > jogador:
            print('Você perdeu, tente novamente um numero MAIOR...')
        else:
            print('Você perdeu, tente novamente um numero MENOR..')
    if ok:
        break

    print('-' * 25)

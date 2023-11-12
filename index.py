from random import randint
from time import sleep
from suporte import *

#programa principal
cabeçalho()
computador = randint(0, 10)
premio = ['Celular', 'Tênis', 'Pc Gamer']
sorteio = randint(0, 3)
ok = False

pessoas = cadastro('Quantos participantes?')
tot = len(pessoas)
cont = 0
while cont != tot:
    print(f'Paricipante {pessoas[cont]["nome"]} tem 3 tentativas')

    for contador in range(1, 4):
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
                print(f'\033[33mVocê perdeu, tente novamente um numero {"\033[31mMAIOR\033[m"}...\033[m')
            else:
                print(f'\033[31mVocê perdeu, tente novamente um numero {"\033[31mMENOR\033[m"}...\033[m')
        if ok:
            break

        print('-' * 25)
    cont += 1


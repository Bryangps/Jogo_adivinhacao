from random import randint
from time import sleep
from suporte import *


#programa principal
cabecalho()

print('Antes de começar escolha uma das opção abaixo'.center(65).upper())
print('[1] - Adiconar participante\n'
      '[2] - Listar paticipantes\n'
      '[3] - Remover participantes\n'
      '[4] - Jogar\n')

while True:
    try:
        opcao = int(input('opção: '))
    except (ValueError, TypeError):
        print('\033[31mOps, aconteceu um ERRO, informe um numéro (1 à 5)\033[m')
        print('~' * 75)
    except KeyboardInterrupt:
        print('\nTchau! Volte sempre')
        break
    else:
        if opcao == 1:
            print('-' * 60)
            Pessoa.cadastros(nome(), idade())
            print('-' * 60)
            break
        elif opcao == 2:
            print('-' * 60)
            print('Pessoa cadastradas'.center(45))
            Pessoa.listar_pessoas()
            print('-' * 60)
            break
        elif opcao == 3:
            print('-' * 60)
            Pessoa.remover_participantes()
            print('-' * 60)
            break
        elif opcao == 4:
            participantes = []
            with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    lista = linha.split(',')
                    participantes.append(lista)

            total_pessoa = len(participantes)
            contador = 0
            print('-' * 60)
            while contador != total_pessoa:
                computador = randint(0, 10)
                print(f'Paricipante {participantes[contador][0]} tem 3 tentativas')
                for tentativas in range(1, 4):
                    print(f'Tentativa - {tentativas} ')
                    jogador = verificacao('Digite um numero (0 à 10):')
                    if jogador < 0:
                        break
                    sleep(0.8)
                    if jogador != computador:
                        if computador > jogador:
                            print(f'\033[31mVocê perdeu, tente novamente um numero {"\033[33mMAIOR\033[m"}...\033[m')
                        else:
                            print(f'\033[31mVocê perdeu, tente novamente um numero {"\033[33mMENOR\033[m"}...\033[m')
                    else:
                        print(f'PARABÉNS {participantes[contador][0]}!, Você ganhou.')
                        print('-' * 60)
                        break
                    print('-' * 60)
                contador += 1
            if contador == total_pessoa:
                print('Obrigador por participarem, volte sempre')
                break
        else:
            print('Opição invalida, tente novamente umas das opção acima')
            print('-' * 75)


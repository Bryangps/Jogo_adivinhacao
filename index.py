from random import randint
from time import sleep
print('-=' * 40)
print('{:^80}'.format('TENTE ADIVINHAR O NÚMERO DE 0 À 10 QUE ESTOU PENSANDO...'))
print('{:^80}'.format('VOCÊ TEM 4 TENTATIVAS. BOA SORTE!!'))
print('O ganhador, ganha um PC GAMER.')
print('-=' * 40)
computador = randint(0, 10)
premio = ('Celular', 'Tênis', 'Pc Gamer')
sorteio = randint(0, 3)
pessoas = 1
contador = 0
while pessoas != 5:
    for cont in range(0, 4):
        print(f'{pessoas} PARTECIPANTE.')
        while True:
            jogagor = int(input('Digite um número: '))
            if (jogagor >= 0) and (jogagor <= 10):
                break
            print('Número invalido. Tente novamente')
        contador += 1
        sleep(1)
        if jogagor == computador:
            print('PARABÉNS, Você me venceu')
            print(f'Você ganhou um {premio[sorteio]}')
            print('-=' * 15)
            break
        else:
            if computador > jogagor:
                print('Você perdeu, tente novamente um numero maior...')
            else:
                print('Você perdeu, tente novamente um numero menor...')
        print('-=' * 20)

    pessoas += 1

print(f'Tentativas {contador}')
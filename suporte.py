def cabeçalho():
    print('-' * 70)
    print(f'TENTE ADIVINHAR O NÚMERO DE 0 À 10 QUE ESTOU PENSANDO...'.center(70))
    print('VOCÊ TEM 4 TENTATIVAS. BOA SORTE!!'.center(70))
    print('-' * 70)


def verificação(msg):
    while True:
        jogador = int(input(f'{msg} '))
        if 0 <= jogador <= 10:
            break
        else:
            print('ERRO! Informe um valor entre 0 é 10')
    return jogador



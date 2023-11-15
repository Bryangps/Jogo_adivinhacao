def cabeçalho():
    print('-' * 70)
    print(f'TENTE ADIVINHAR O NÚMERO DE 0 À 10 QUE ESTOU PENSANDO...'.center(70))
    print('VOCÊ TEM 3 TENTATIVAS. BOA SORTE!!'.center(70))
    print('-' * 70)


def verificação(msg):
    while True:
        try:
            jogador = int(input(f'{msg} '))
        except (ValueError, TypeError):
            print('Erro! Informe um numero interio')
        except (KeyboardInterrupt):
            print('Volte sempre')
            break
        else:
            if 0 <= jogador <= 10:
                break
            else:
                print('Erro! Escolha um numero de 0 à 10')
    return jogador


def cadastro(msg):
    lista = list()
    partici = dict()
    quantidade = int(input(f'{msg} '))
    for c in range(0, quantidade):
        partici['nome'] = str(input('Nome: ')).title().strip()
        partici['idade'] = int(input('Idade: '))
        lista.append(partici.copy())
        print('-' * 40)
    return lista




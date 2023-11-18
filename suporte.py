def cabecalho():
    print('-' * 70)
    print(f'TENTE ADIVINHAR O NÚMERO DE 0 À 10 QUE ESTOU PENSANDO...'.center(70))
    print('VOCÊ TEM 3 TENTATIVAS. BOA SORTE!!'.center(70))
    print('-' * 70)


def verificacao(num):
    while True:
        try:
            jogador = int(input(f'{num} '))
        except (ValueError, TypeError):
            print('Erro! Informe um numero interio')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return -1
        else:
            if 0 <= jogador <= 10:
                return jogador
            else:
                print('Erro! Escolha um numero de 0 à 10')


def quantidade(msg):
    while True:
        try:
            pessoa = int(input(f'{msg} '))
        except (ValueError, TypeError):
            print('Erro! Informe um numero interio')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return 0
        else:
            return pessoa


def nome():
    while True:
        try:
            name = str(input('Nome: ')).title().strip()
        except (ValueError, TypeError):
            print('Erro! Valor digitado invalido, informe seu nome')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return ''
        else:
            if not name:
                print('O campo não pode estar vazio')
            elif name.isdigit():
                print('Ops! O campo não pode ser um número.')
            else:
                return name


def idade():
    while True:
        try:
            ide = int(input('Idade: '))
        except (ValueError, TypeError):
            print('Erro! Informe um numero interio')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return ''
        else:
            return ide


def cadastro(qtd):
    lista = list()
    partici = dict()
    for c in range(0, qtd):
        partici['nome'] = nome()
        if partici['nome'] == '':
            break
        partici['idade'] = idade()
        if partici['idade'] == '':
            break
        print('-' * 40)
        lista.append(partici.copy())
    return lista

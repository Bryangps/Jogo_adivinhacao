def cabecalho():
    print('-' * 70)
    print(f'TENTE ADIVINHAR O NÚMERO DE 0 À 10 QUE ESTOU PENSANDO...'.center(70))
    print('VOCÊ TEM 3 TENTATIVAS. BOA SORTE!!'.center(70))
    print('-' * 70)


def verificacao(msg):
    while True:
        try:
            jogador = int(input(f'{msg} '))
        except (ValueError, TypeError):
            print('Erro! Informe um numero interio')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            jogador = -1
            break
        else:
            if 0 <= jogador <= 10:
                break
            else:
                print('Erro! Escolha um numero de 0 à 10')
    return jogador


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


def cadastro(qtd):
    lista = list()
    partici = dict()
    ok = False
    for c in range(0, qtd):
        while True:
            try:
                partici['nome'] = str(input('Nome: ')).title().strip()
            except (ValueError, TypeError):
                print('Erro! Valor digitado invalido, informe seu nome')
            except (KeyboardInterrupt, NameError):
                print('\nVolte sempre')
                ok = True
                break
            else:
                if not partici['nome']:
                    print('O campo não pode estar vazio')
                elif partici['nome'].isdigit():
                    print('Ops! O campo não pode ser um número.')
                else:
                    break

        while not ok:
            try:
                partici['idade'] = int(input('Idade: '))
            except (ValueError, TypeError):
                print('Erro! Informe um numero interio')
            except KeyboardInterrupt:
                print('\nVolte sempre')
            else:
                lista.append(partici.copy())
                print('-' * 40)
                break
    return lista



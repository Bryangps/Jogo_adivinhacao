import csv
import os


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
            print()
            return -1
        else:
            if 0 <= jogador <= 10:
                return jogador
            else:
              print('Erro! Escolha um numero de 0 à 10')


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
            ida = int(input('Idade: '))
        except (ValueError, TypeError):
            print('Erro! Informe um numero interio')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return ''
        else:
            return ida


class Pessoa:
    @staticmethod
    def cadastros(name, age):
        with open('pessoas.csv', 'r', encoding='utf-8') as file:
            leitor = csv.reader(file)
            palavra_existente = [linha[0] for linha in leitor]

        if name not in palavra_existente:
            with open('pessoas.csv', 'a', encoding='utf-8') as arquivo:
                escreve = csv.writer(arquivo, lineterminator='\n')
                escreve.writerow([name, age])
                print('Cadastrado com sucesso.')
        else:
            print('Já existe')

    @staticmethod
    def listar_pessoas():
        with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                name, age = linha.rstrip().split(',')
                print(f'{name} - {age} anos')

    @staticmethod
    def remover_participantes():
        if not os.path.exists('pessoas.csv'):
            print('Lista de cadastro está vazia')
        with open('pessoas.csv', 'w', encoding='utf-8') as arquivo:
            arquivo.write(' ')
            print('Removio com sucesso')

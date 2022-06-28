"""
Exercício 06 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    5
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    -1
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    3
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    15
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""

    num_1 = float(input('Digite o 1° número: '))
    num_2 = float(input('Digite o 2° número: '))
    num_3 = float(input('Digite o 3° número: '))
    if num_1 > num_2 and num_1 > num_3:
        print(f'O maior número é: {num_1}')
    elif num_2 > num_3 and num_2 > num_1:
        print(f'O maior número é: {num_2}')
    elif num_3 > num_2 and num_3 > num_1:
        print(f'O maior número é: {num_3}')
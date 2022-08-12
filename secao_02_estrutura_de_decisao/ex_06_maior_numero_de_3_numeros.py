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

    #x = float(input('Digite o 1° número: '))
    #y = float(input('Digite o 2° número: '))
    #z = float(input('Digite o 3° número: '))
    if x > y and x > z:
        print(f'{x}')
    elif y > z and y > x:
        print(f'{y}')
    elif z > y and z > x:
        print(f'{z}')
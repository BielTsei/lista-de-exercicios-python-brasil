"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""

    x = float(input('Digite o 1° número: '))
    y = float(input('Digite o 2° número: '))
    z = float(input('Digite o 3° número: '))
    if x > y and x > z:
        print(f'Maior: {x}')
    elif y > z and y > x:
        print(f'Maior: {y}')
    elif z > y and z > x:
        print(f'Maior: {z}')

    if x < y and x < z:
        print(f'Menor: {x}')
    elif y < z and y < x:
        print(f'Menor:: {y}')
    elif z < y and z < x:
        print(f'Menor: {z}')

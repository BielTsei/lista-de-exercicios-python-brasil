"""
Exercício 03 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Retorne: F - Feminino ou M - Masculino. Para quaisquer outros valores, retorne Sexo Inválido.

    >>> f_ou_m("F")
    'F - Feminino'
    >>> f_ou_m("M")
    'M - Masculino'
    >>> f_ou_m('Z')
    'Sexo inválido'
    >>> f_ou_m(1)
    'Sexo inválido'
"""


def f_ou_m(sexo):
    """Escreva aqui em baixo a sua solução"""


    #sexo = str(input('Digite a Feminino ou Masculino (F para feminino e M para Masculino): ')).upper()
    if sexo == 'F':
        print("'F - Feminino'")
    elif sexo == 'M':
        print("'M - Masculino'")
    elif sexo != 'F' 'M':
        print("'Sexo inválido'")

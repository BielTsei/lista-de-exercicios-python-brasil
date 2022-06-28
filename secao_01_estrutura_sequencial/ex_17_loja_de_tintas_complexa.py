"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão
    sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão
    sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    import math

    metros_qudrados_a_serem_pintados = float(input('Digite a quantidade de metros quadrados a serem pintados: '))
    area_de_folga = metros_qudrados_a_serem_pintados * 1.1
    # Valores
    cobertura_por_metro = 6
    lata = 18
    lata_valor = 80
    galoes = 3.6
    galoes_valor = 25

    litros_a_serem_usados = math.ceil(area_de_folga / cobertura_por_metro)

    numero_de_latas = math.ceil(litros_a_serem_usados / lata)
    numero_de_galoes = math.ceil(litros_a_serem_usados / galoes)

    valor_com_apenas_latas = numero_de_latas * lata_valor
    valor_com_apenas_galoes = numero_de_galoes * galoes_valor

    sobra_de_latas = (lata * numero_de_latas) - litros_a_serem_usados
    sobra_de_galoes = (galoes * numero_de_galoes) - litros_a_serem_usados

    numero_das_latas = math.floor(litros_a_serem_usados / lata)

    litros_faltantes = (litros_a_serem_usados % lata)

    numero_dos_galoes = math.floor(litros_faltantes / galoes)

    valor_da_lata = numero_das_latas * 80
    valor_do_galao = numero_dos_galoes * 25
    valor = valor_do_galao + valor_da_lata

    sobra_otimizada = (lata + galoes) - litros_a_serem_usados

    print(f'Você deve comprar {litros_a_serem_usados:.0f} litros de tinta.')
    print(f'Você pode comprar {numero_de_latas} lata(s) de 18 litros a um custo de R$ {valor_com_apenas_latas}'
          f'. Vão sobrar {sobra_de_latas:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {numero_de_galoes} lata(s) de 3.6 litros a um custo de R$ {valor_com_apenas_galoes}.'
          f' Vão sobrar {sobra_de_galoes:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {numero_de_latas} lata(s) de 18 litros e {numero_de_galoes} galão(ões) '
          f'de 3.6 litros a um custo de R$ {valor}. Vão sobrar {sobra_otimizada:.1f} litro(s) de tinta.')

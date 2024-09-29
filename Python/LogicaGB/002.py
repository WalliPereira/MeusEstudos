# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / 6

latas_18_litros = math.ceil(litros_necessarios / 18)

galoes_3_6_litros = math.ceil(litros_necessarios / 3.6)

custo_latas_18_litros = latas_18_litros * 80
custo_galoes_3_6_litros = galoes_3_6_litros * 25

# Exibir os resultados
print(f'Área a ser pintada: {area} metros quadrados')
print(f'Litros necessários: {litros_necessarios:.2f} litros')
print(f'Latas de 18 litros necessárias: {latas_18_litros} latas')
print(f'Custo total com latas de 18 litros: R$ {custo_latas_18_litros:.2f}')
print(f'Galões de 3,6 litros necessários: {galoes_3_6_litros} galões')
print(f'Custo total com galões de 3,6 litros: R$ {custo_galoes_3_6_litros:.2f}')
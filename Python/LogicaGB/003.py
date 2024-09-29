#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / 6
litros_necessarios *= 1.1

latas_18_litros = math.ceil(litros_necessarios / 18)
galoes_3_6_litros = math.ceil(litros_necessarios / 3.6)

custo_latas_18_litros = latas_18_litros * 80
custo_galoes_3_6_litros = galoes_3_6_litros * 25

latas_18_litros_mistura = math.floor(litros_necessarios / 18)
galoes_3_6_litros_mistura = math.ceil((litros_necessarios - (latas_18_litros_mistura * 18)) / 3.6)

custo_mistura = (latas_18_litros_mistura * 80) + (galoes_3_6_litros_mistura * 25)

print("Opção 1: Comprar apenas latas de 18 litros")
print(f"Quantidade: {latas_18_litros} latas")
print(f"Custo: R$ {custo_latas_18_litros:.2f}")

print("\nOpção 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade: {galoes_3_6_litros} galões")
print(f"Custo: R$ {custo_galoes_3_6_litros:.2f}")

print("\nOpção 3: Misturar latas e galões")
print(f"Quantidade: {latas_18_litros_mistura} latas e {galoes_3_6_litros_mistura} galões")
print(f"Custo: R$ {custo_mistura:.2f}")
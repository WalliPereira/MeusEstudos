# Solicita o tamanho da área em metros quadrados
area = float(input("Informe o tamanho da área a ser pintada (em m²): "))

# Cálculo da quantidade de tinta necessária
litros_necessarios = area / 3  # 1 litro cobre 3 m²
latas_necessarias = -(-litros_necessarios // 18)  # Arredondando para cima

# Cálculo do preço total
preco_total = latas_necessarias * 80.00  # R$ 80,00 por lata

# Exibe os resultados
print(f"Quantidade de latas de tinta a serem compradas: {int(latas_necessarias)}")
print(f"Preço total: R$ {preco_total:.2f}")

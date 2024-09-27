1. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
   Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
   Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metroInput = float(input("Digite a quantidade de Metros: "))

coberturaLitro = 3
litroPLata = 18

litroNecessario = metroInput / coberturaLitro

latasNecessarias = -(-litroNecessario // litroPLata)

valorTotal = latasNecessarias * 80.00

print(f'A quantidade de latas a serem compradas são: {int(latasNecessarias)} ')
print(f'E o valor total de todas latas inclusas são: R$ {valorTotal:.2f} ')

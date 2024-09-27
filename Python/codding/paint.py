metroInput = float(input("Digite a quantidade de Metros: "))

coberturaLitro = 3
litroPLata = 18

litroNecessario = metroInput / coberturaLitro

latasNecessarias = -(-litroNecessario // litroPLata)

valorTotal = latasNecessarias * 80.00

print(f'A quantidade de latas a serem compradas são: {int(latasNecessarias)} ')
print(f'E o valor total de todas latas inclusas são: R$ {valorTotal:.2f} ')

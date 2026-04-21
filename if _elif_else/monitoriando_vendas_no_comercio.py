maca = int(input('Digite a quantidade de maçãs vendidas: '))
banana = int(input('Digite a quantidade de bananas vendidas: '))


if maca > banana:
    print('AS maçãs tiveram mais vendas')

elif banana > maca:
    print('As bananas tiveram mais vendas')
else:
    print('As vendas foram iguais')
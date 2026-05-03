lista = []
soma = 0

try:

    for numero in lista:
        soma += numero
    media = soma / len(lista)
    print(f'Media dos valores da lista: {media}')

except ZeroDivisionError:

    print('A lista esta vazia')

lista_numero = [12, 56, 98, 125, 45]
total = 0


try:
    for lista in lista_numero:
        total += lista

    print(f'soma dos numeros: {total}')

except ValueError:

    print('ocorreu um erro inesperado, devido a um ou mais valores tipos diferentes na lista')





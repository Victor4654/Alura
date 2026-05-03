lista_nomes = ["victor", "joão", "maria", "fabio"]
print(f"Lista atual: {", ".join(lista_nomes)}")

errado = str(input("Digite o nome incorreto: "))

if errado in lista_nomes:

    posicao = lista_nomes.index(errado)
    correto = str(input("Digite o nome correto: "))
    lista_nomes.remove(errado)
    lista_nomes.insert(posicao, correto)
    print(f"O nome {errado} foi substituido por {correto}")
    print(f"Lista atualizada: {", ".join(lista_nomes)}")

else:
    print("Nome nao encontrado na lista.")
    print(f"Lista: {", ".join(lista_nomes)}")

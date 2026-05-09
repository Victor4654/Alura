lista_compras = ["açucar","leite","pão","queijo","tapioca"]

verificar = input("Digite o item que voçê quer verificar: ")

if verificar in lista_compras:
    print("O item ja foi comprado.")
else:
    print(f"O item {verificar} precisa ser comprado.")

nome = None
quantidade = None
lista = {}
while True:

    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    sair = input("Digite qualquer tecla para continuar ou digite 1 para sair.")
    #lista.setdefault(nome , quantidade)
    lista[nome] = quantidade
    if int(sair) == 1:
        break

print(lista)
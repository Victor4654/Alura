estoque = {
    "Caderno universitário": 50, 
    "Caneta azul": 120, 
    "Borracha branca": 30 
}

print(f"lista do estoque atual: {estoque}\n")

nome = str(input("Digite o nome do produto a ser atualizado: "))
nova_quantidade = int(input("Nova quantidade: "))

if nome in estoque:
    estoque.update({nome : nova_quantidade})
    print(f"Lista atualizada: {estoque}")
else:
    print("Produto não encontrado no estoque.")
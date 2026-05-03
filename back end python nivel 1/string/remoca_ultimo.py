pedido = list(input("Pedidos feitos (separado por vírguça): ").split(", "))
pedido.pop()
print(", ".join(pedido))
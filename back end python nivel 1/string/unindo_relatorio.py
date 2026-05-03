estoque1 = (input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = (input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque = estoque1 + estoque2
print(f"Estoque combinado: \n{", ".join(estoque)}")




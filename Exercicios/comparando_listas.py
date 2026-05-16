lista1 = set(input("Lista de Laura: ").lower().split(", "))
lista2 = set(input("Lista de Ana: ").lower().split(", "))
comum = lista1.intersection(lista2)
lista1_exclusivo = lista1.difference(lista2)
lista2_exclusivo = lista2.difference(lista1)

print(f"\nItens em ambas as listas: {", ".join(comum)}\n")
print(f"Itens exclusivos de Laura: {", ".join(lista1_exclusivo)}\n")
print(f"Itens exclusivos de Ana: {", ".join(lista2_exclusivo)}")
participantes = {

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
}

for workshop, nomes in participantes.items():
    print(f"{workshop} : {", ".join(nomes)}")


remover = str(input("Nome do participante a ser removido: "))

for workshop, nomes in participantes.items():
    nomes.discard(remover)


print("\nLista atualizada de participantes:\n")
for workshop, nomes in participantes.items():
    print(f"{workshop} : {", ".join(nomes)}")


      


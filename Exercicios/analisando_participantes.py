participantes = {
    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35
}

print("Lista de participantes.\n\n")

nomes = None
idade = None

print(f"Nome dos participantes: {", ".join(nomes for nomes in participantes.keys())}\n")
#print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}") 
print(f"Idades dos participantes: {", ".join(str(idade) for idade in participantes.values())}\n")
print("Participantes e suas idades:")

for chave,valor in participantes.items():
    print(f"- {chave} : {valor}")
    


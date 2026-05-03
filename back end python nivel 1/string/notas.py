n = int(input("Digite a quantidade de notas: "))
notas = []
for numero in range(n):
    notas.append(int(input("Nota: ")))


print(f"Notas originais: {notas}")
notas.sort()
print(f"\nNotas ordenadas: {notas}")


                 


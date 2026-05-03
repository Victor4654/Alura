texto = input("Digite um texto: ").strip()
vogais = ["a","e","i","o","u"]
total = 0 

for letras in vogais:

    quantidade = texto.count(letras)
    total = quantidade + total

print(f"O texto contém {total} vogais.")



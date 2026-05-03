texto = input("Digite um texto: ").split()
palavras_longas = []

for palavras in texto:
    if len(palavras) > 10:
        palavras_longas.append(palavras)


if palavras_longas:
    print(f"Palavras longas encontradas: {", ".join(palavras_longas)}")
else:
    print("Nenhuma palavra longa foi encontrada no texto")

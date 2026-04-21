def quantidade_carcteres(palavra):

    return len(palavra.replace(" ",""))

palavra = input("Digite uma palavra: ")
tamanho = quantidade_carcteres(palavra)

print(f"Essa palavra tem {tamanho} caracteres.")
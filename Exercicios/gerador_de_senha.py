import random

def gerador():
    
    lista = "123456789!@#$%¨&*_-=+|/?:><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    gerador_senha = []
    for senha in lista:
        gerador_senha.append(senha)

    senha = random.choices(gerador_senha, k=12)
    return "".join(senha)

print(f"senha gerada: {gerador()}")





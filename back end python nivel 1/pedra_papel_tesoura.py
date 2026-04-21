import random

def pedra_papel_tesoura():
        
    escolha = input("Escolha: pedra,papel ou tesoura: ").strip().lower()
    lista = ["pedra","papel","tesoura"]
    maquina = random.choice(lista)

    if escolha not in lista:
        print("Escolha inválida")
        return
    
    print(f"computador escolheu: {maquina}")
    

    if escolha == maquina:
        print("Empate!")
    elif (
        (escolha == "papel" and maquina == "pedra") or
        (escolha == "pedra" and maquina == "tesoura") or 
        (escolha == "tesoura" and maquina == "papel")):
        print("Voçê venceu!")
    else:
        print("Voçê perdeu!")


pedra_papel_tesoura()
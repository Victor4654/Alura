def saudacao(palavra):
    if palavra < 12:
        print("Bom dia")
    elif 12<= palavra <= 18:
        print("Boa tarde")
    else:
        print("Boa noite")


hora_atual = float(input("Digite a hora atual (0-23): "))
comprimento = saudacao(hora_atual)

print(comprimento)
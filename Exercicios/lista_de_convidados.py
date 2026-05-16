saida = 0
convidado = set({})
while saida != 1:

    nome = input("Digite o nome do convidado: ").strip().title()

    match nome:

        case "Sair":
            saida += 1

        case _:
            convidado.add(nome)
        


print(f"Convidados confirmados: {" | ".join(convidado)}")



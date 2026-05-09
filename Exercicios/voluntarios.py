lista_voluntarios = []

while True:

    voluntario = str(input("Digite o nome do voluntário(ou 'sair' para encerrar): "))
    if voluntario.lower() != "sair":
        lista_voluntarios.append(voluntario.title())
    else:
        break

print(f"\nVoluntários registrados: {", ".join(lista_voluntarios)}")

    
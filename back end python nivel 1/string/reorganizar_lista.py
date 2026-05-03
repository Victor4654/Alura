lista_convidados = ["Ana", "Pedro", "Carlos"]
print(f"Lista atual de convidados: {", ".join(lista_convidados)}")
novo_convidado = str(input("Digite o nome do novo convidado: ").title())
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
lista_convidados.insert(posicao-1,novo_convidado)
print(f"Lista atualizadas de convidados: {lista_convidados}")
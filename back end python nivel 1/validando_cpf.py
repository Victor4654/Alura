cpf = input("Digite seu CPF: ").strip()

if len(cpf) == 11 and cpf.isdigit() == True:
    print("CPF válido.")
elif len(cpf) == 11 and cpf.isalnum() == True:
    print("Erro: o CPF deve conter apenas números.")
elif len(cpf) != 11:
    print("Erro: o CPF deve ter exatamente 11 dígitos.")


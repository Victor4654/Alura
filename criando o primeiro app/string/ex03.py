name = 'victor teles'
senha = 'xcv5465'
print("LOGIN\n")
nomelogin = str(input("Nome:"))
senhalogin = str(input("Senha: "))

if nomelogin == name and senhalogin == senha:
    print("Login realizado com sucesso")
else:
    print("\nERRO\n")
    print("senha ou nome de usuário incorreta")

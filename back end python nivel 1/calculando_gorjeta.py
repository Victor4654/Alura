conta = float(input("Digite o valor da conta: "))
gorjeta = float(input("Digite o valor da porcentagem da gorjeta: "))

print(f"Valor da gorjeta: {conta*(gorjeta/100):.2f}")
print(f"Total a pagar: {conta*(1+(gorjeta/100)):.2f}")


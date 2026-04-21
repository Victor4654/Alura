
def Valor_total(valores):

    valor = list(map(float,valores.split()))
    numero = 0
    for total in valor:
        numero += total

    return f"O total de vendas foi: {numero}"


numero = input("Digite os valores das vendas: ")

print(Valor_total(numero))

        

#valores = input("Digite os valores das vendas: ").split() 
#total = sum(map(float, valores)) 
#print(f"O total de vendas foi: {total}") 






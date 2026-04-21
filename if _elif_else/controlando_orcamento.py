limite = 3000

despesas_do_mes = float(input('Digite o total de despesas do mês (R$): '))

if despesas_do_mes > limite:
    print('Atenção! voçê ultrapassou o limite do orçamento')
else:
    print('Voçê esta dentro do orçamento')
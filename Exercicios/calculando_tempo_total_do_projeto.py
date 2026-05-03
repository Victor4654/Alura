A = int(input('Informe os dias para a atividade A: '))
B = int(input('Informe os dias para a atividade B: '))
C = int(input('Informe os dias para a atividade C: '))

if A >= 0 and B >= 0 and C >= 0:
    print(f'O tempo total do projeto foi :{A+B+C} Dias')

else:
    print('Erro: os dias nao podem ser negativos')

    

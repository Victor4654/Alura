temperatura_atual = float(input('Digite a temperatura atual: '))

if temperatura_atual > 25:
    print('Alerta! Temperatura acima do limite permitido.')

elif temperatura_atual <= 0:
    print('Temperatura abaixo de 0')
else:
    
    print('Temperatura normal')
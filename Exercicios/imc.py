peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Abaixo do peso normal')
elif 18.5<=imc<25:
    print('Peso normal')
elif imc >= 25:
    print('Acima do peso')

else:
    print('Erro!: valor incorreto digitado')
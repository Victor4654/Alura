def quadrante():
    x = float(input("x: "))
    y = float(input("y: "))

    if x > 0 and y > 0:
        print("Primeiro quadrante")
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else:
        print('Ponto de origem')

quadrante()


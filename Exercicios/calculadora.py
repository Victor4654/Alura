def calculadora():

    try:

        a = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        b = float(input("Digite o segundo número: "))
        
        if operacao == "+":
            print(f"Resultado: {a+b}")
        elif operacao == "-":
            print(f"Resultado: {a-b}")
        elif operacao == "*":
            print(f"Resultado: {a*b}")
        elif operacao == "/":
            print(f"Resultado: {a/b}")
        else:
            print("Operação inválida!")

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida")



calculadora()



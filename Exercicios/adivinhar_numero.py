import random

def adivinhar_numero():
    numero = random.choice(range(100))
    tentativas = 0
    while True:

        try: 
            adivinhe = int(input("Tente adivinhar o número (1-100): "))

            if not 1<= numero <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 a 100.")
            tentativas += 1
            
            if adivinhe == numero:
                print(f"Parabéns! Voçê acertou o número {numero}, número de tentativas {tentativas}.")
                break
            elif adivinhe < numero:
                print(f"Muito baixo! Tente novamente: {numero-adivinhe}")
            elif adivinhe > numero:
                print(f"Muito alto! Tente novamente: {adivinhe-numero}")
        except ValueError as e:
            print(f"Entrada inválida: {e}")



adivinhar_numero()
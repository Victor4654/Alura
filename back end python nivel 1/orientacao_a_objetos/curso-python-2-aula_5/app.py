from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebidas("Suco de Abacaxi", 6.0, "grande")
prato_paozinho = Prato("Pãozinho", 2.00, "o melhor pão da cidade")



def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
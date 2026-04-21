import os

restaurantes = [{'nome':'praça','categoria':'japonesa','ativo':False},
                {'nome':'Kalilandia','categoria':'pizza','ativo':True},
                {'nome':'burger king','categoria':'hamburguer','ativo':False},
                {'nome':'rei da tapioca','categoria':'tapioca','ativo':True}]



def exibir_nome_do_programa():
    print("\nS̸͔̝͉̽͆͑a̴̦̺̠͒̈́͊b̵̻̟̠͛̚͝o̴͙͕̞̿͊̚r̵̫͓͉̀̀͝ ë̵͍͍͔́̈́̕x̵͍͉̠̐̔̓p̵͔͎̽̐͊r̵̙͓͚͛̐e̵̦̫̼͆͌͘s̴̟͙͇͌́͝s̸͚̺͊͋̚ \n")

def exibir_opcoes():
    print("1. Cadastrar restaurantes")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system('cls')#limpar no windows
    #os.system('clear')#limpar no mac
    print("Finalizando o app")

def opcao_invalida():
    print("Opção inválida!\n")
    int(input("Digite uma tecla para voltar ao menu principal"))
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = str(input("Digite o nome do restaurante: ")).strip().title()

    restaurantes.append(nome_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def listar_restaurantes():
    os.system('cls')
    print("Restaurantes cadastrados:\n")

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f'{nome.title()} | {categoria.title()} | {ativo}')


    input("Digite uma tecla para voltar ao menu principal.")
    main()



def escolher_opcao():
     
     try:

        opcao_escolhida = int(input("Escolha uma opção: "))
    
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

     except:
        opcao_invalida()
    


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
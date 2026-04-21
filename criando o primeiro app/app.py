import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Kalilandia','categoria':'Pizza','ativo':True},
                {'nome':'Burger King','categoria':'Hamburguer','ativo':False},
                {'nome':'Rei Da Tapioca','categoria':'Tapioca','ativo':True}]


def voltar_ao_menu_principal():
    '''essa função volta a funcao main em todas as outras funções'''

    input("\nDigite uma tecla para voltar ao menu principal.")
    main()


def exibir_nome_do_programa():
    '''Mostra o nome do programa na funcao principal main'''

    print("\nS̸͔̝͉̽͆͑a̴̦̺̠͒̈́͊b̵̻̟̠͛̚͝o̴͙͕̞̿͊̚r̵̫͓͉̀̀͝ ë̵͍͍͔́̈́̕x̵͍͉̠̐̔̓p̵͔͎̽̐͊r̵̙͓͚͛̐e̵̦̫̼͆͌͘s̴̟͙͇͌́͝s̸͚̺͊͋̚ \n")


def exibir_subtitulo(texto):
    
    '''exibi subtitulos personalisveis nas outras funções'''
    os.system('cls')
    linha = '*' * (len(texto)+4)
    print(linha)
    print(texto.strip().title())
    print(linha,'\n')


def exibir_opcoes():
    
    '''exibi as opções do programa para o usuario'''

    print("1. Cadastrar restaurantes")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    
    '''finaliza o aplicativo limpando a tela e mostrando a mensagem dentro da função'''
    os.system('cls')#limpar no windows
    #os.system('clear')#limpar no mac
    print("Finalizando o app...")


def opcao_invalida():
    '''retorna mensagem opcao invalida e retorna a funcao main'''
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():

    '''cadastra novos restaurantes, recebendo inputs pelo usuario do nome do restaurante e categoria do restaurante'''

    exibir_subtitulo("cadastrar restaurantes")
    nome_do_restaurante = str(input("Digite o nome do restaurante: ")).strip().title()
    categoria_do_restaurante = str(input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")).strip().title()

    restaurantes.append({'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante,'ativo':False})

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()


def listar_restaurantes():

    '''exibe a lista de todos os restaurantes cadastrados'''
    exibir_subtitulo("Listando restaurantes")
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:

        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        
        print(f'- {nome.title().ljust(20)} | {categoria.title().ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()


def alternar_estado_restaurante():

    '''alternar o estado dos restaurantes para True or False , pelo nome fornecido para modificar o status para ativo ou desativado'''

    exibir_subtitulo('Alterando o estado do restaurante\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ').lower()

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante nao encontrado')
    
    voltar_ao_menu_principal()


def escolher_opcao():
     
     '''Nessa funcao pede para o usuário escolher uma opção para proseguir para outra funcao, e tem um try e except para caso o usuário digite algo fora do pedido'''
     
     try:

        opcao_escolhida = int(input("Escolha uma opção: "))
    
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

     except:
        opcao_invalida()
    

def main():

    '''funcao principal do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
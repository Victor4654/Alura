

def converter_para_inteiro(lista):
    telefone = list(map(int,lista))
    return telefone


def verificando_conversão(telefone_convertido):

    verificando = False
    for numero_inteiro in telefone_convertido:
        if not isinstance(numero_inteiro,int):
            return "Erro na conversão"
        
    return "todos os números foram convertidos corretamente!"




numero_telefone = ["79999976819","79989224022","79999180175"]

print(verificando_conversão(converter_para_inteiro(numero_telefone)))


        












    








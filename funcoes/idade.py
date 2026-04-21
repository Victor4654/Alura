
def idade_atual(ano_nascimento,ano_atual):
    return ano_atual - ano_nascimento

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
print(f'A idade atual é {idade_atual(ano_nascimento,ano_atual)}')
from conta_bancaria import ContaBancaria

class Pessoa:
    def __init__(self, nome, idade, profissao):

        self.nome = str(nome).title()
        self.idade = int(idade)
        self.profissao = str(profissao).title()
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}"

    @property
    def saudacoes(self):
        if self.profissao:
            return f"Olá, sou {self.nome}! Trabalho como {self.profissao}"
        else:
            return f"Olá, sou {self.nome}"

    def aniversario(self):
        self.idade += 1
        


pessoa1 = Pessoa("victor teles farias", 25, "engenheiro de dados")
pessoa2 = ContaBancaria("victor teles farias", 4568.45)
pessoa2.ativar_conta
print(pessoa1)
print(pessoa1.saudacoes)
print(pessoa2)
        

        
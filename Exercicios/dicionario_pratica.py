dados = {'nome':'Mark','idade':500,'cidade':'viltrum'}

print(dados)
dados['idade'] = 700
dados['profissão'] = 'imperador'
dados['altura']= 1.80
print('\n',dados)
dados.pop('altura')
print(dados)

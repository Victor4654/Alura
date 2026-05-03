notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
soma = 0
media = 0
for nota in notas:
    soma += float(nota)
    media = soma/(len(notas))

print(f"Média final da turma: {media:.2f}")

    
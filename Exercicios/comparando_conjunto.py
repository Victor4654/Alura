equipe_a = set(a.strip() for a in input("Digite o nome da tarefa: ").lower().split(", "))
equipe_b = set(b.strip() for b in input("Digite o nome da tarefa: ").lower().split(", "))

tarefas_totais = equipe_a.union(equipe_b)
print(f"Tarefas finais: {", ".join(tarefas_totais)}")

remover_tarefa = input("Digite a tarefa a ser removida: ")

if remover_tarefa in tarefas_totais:
    tarefas_totais.remove(remover_tarefa)

print(f"\nTarefas finais: {", ".join(tarefas_totais)}")


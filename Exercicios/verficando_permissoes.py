principal = set("leitura, escrita, execução, compartilhamento".split(", "))
secundario = set("leitura, escrita".split(", "))
principal2 = set("eitura, escrita, execução, compartilhamento ".split(", "))
secundario2 = set("leitura, exclusão".split(", "))

if principal.issuperset(secundario):
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principais.")


if principal2.issuperset(secundario2):
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principais.")

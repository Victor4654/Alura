texto1 = set("O sol brilha forte no céu azul".lower().split())
texto2 = set("O céu azul anuncia um dia de sol intenso".lower().split())
print(texto1)
print(texto2)
comum = texto1.intersection(texto2)
print(comum)

#texto1 = set(input("Texto1: ").lower().split())
#texto2 = set(input("Texto1: ").lower().split())
#print(texto1)
#print(texto2)
#comum = texto1.intersection(texto2)
#print(comum)


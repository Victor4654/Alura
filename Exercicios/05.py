numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['sayure','monika','magnolia','saint']
ano_nascimento = [2001,2026]
n = 0


print('Numeros de um a 10:\n')
for numero in numeros:
    if numero % 2 != 0:
        n += numero
    print(numero)

print('\nnumeros em ordem reversa\n')
for rev in reversed(numeros):
    print(rev)



print(f'\nsoma dos números impares :{n}')
print('\nnomes:\n')
for nome in nomes:
    print(nome)

print('\nanos:\n')
for ano in ano_nascimento:
    print(ano)


print('tabuada de 1 a 10')
N = int(input('digite um numero para a ver a tabuada\n'))

for i in range(11):
    print(f'{N} x {i} = {N*i}')




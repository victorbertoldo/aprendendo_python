'''x = []

for  i in range(1,1001):
    x.append(i)
'''
x = list(range(1,1001)) # criar lista de valores sem usar laço
print(x)

y = [1,2,3,4,5]
print(y)
z = int(input('Digite o valor que quer apagar da lista:'))

if z in y:
    y.remove(z)
    print(f'O valor {z} foi removido')
else:
    print('Nenhum valor foi removido')
print(y)

# Lista de listas

x = [['victor',31], ['Jão', 30], ['Zé',50]]

# mostrar segundo valor da primeira lista
print(x[0][1])
# mostrar primeiro valor  da terceira lista
print(x[2][0])
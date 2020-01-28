'''
fazer um programa que verifique e mostre os numeros entre 1000 e 2000(inclusive) que,
divido por 11, seu mod (resto) seja 5

'''

lista = []
for i in range(1000,2001):
    if i % 11 == 5:
        lista.append(i)
print(lista)
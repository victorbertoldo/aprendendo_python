def mostrarNatela():
    print('hello world')
    print('end')

mostrarNatela()

def soma(n1, n2):
    print(f'a soma é {n1+n2}')

x = []
y = int(input('digite um valor:'))
x.append(y)
print(x)
y = int(input('digite outro valor:'))
x.append(y)
print(x)

soma(x[0],x[1])



def retornaMaior(*list): #uma tupla é imutavel, diferente de uma lista
    print(max(list))
retornaMaior(1,2,3)

'''
[] lista
{} dicionario
() tupla
'''
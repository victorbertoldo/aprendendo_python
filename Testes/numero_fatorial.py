x = int(input('Digite o numero para calcular o n! :'))
fatorial =x
for i in range(x,1,-1):
    fatorial = fatorial * (i-1)
print('O n! de {} é {}'.format(x,fatorial))
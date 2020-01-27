x = 0
while x < 10:
    print('1')
    x = x +1

decisao = 0

while decisao != 3:
    decisao = int(input('Digite sua decisão:'))
    if decisao == 3:
        print('Decisão Certa!')
    else:
        print('Decisão errada!')

print('Final')



decisao = 0

while True:
    decisao = int(input('Digite sua decisão:'))
    if decisao == 3:
        print('Decisão Certa!')
        break # Este comando encerra o laço
    else:
        print('Decisão errada!')

print('Final')
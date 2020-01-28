opcao = 0

while True:
    opcao = int(input('pressione qualquer numero para continuar e -1 para sair:'))
    if opcao == -1:
        break
    else:
        idades = []
        idades.append(int(input('Digite uma idade:')))
print(f'A média das idades é:{sum(idades)/len(idades)}')

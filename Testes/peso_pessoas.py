lista_peso = []

for i in range(1,8):
    print('Preencha o peso de 7 pessoas!')
    peso = int(input(f'Digite o peso da pessoa nº {i}:'))

    lista_peso.append(peso)

media = sum(lista_peso) / i
lista_peso.sort(reverse=True)

qtd = 0

for j in range(0,7):
    #print(lista_peso[j])
    if lista_peso[j] >= 90:
        qtd += 1

print(f'A quantidade de pessoas com peso acima de 90 kg é:{qtd}.')
print(f'A média dos pesos é {media}.')

#print(lista_peso)
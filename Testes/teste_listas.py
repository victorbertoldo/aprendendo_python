
idade = [18,20,30,40,50,60,15,12]
#idade = []

#inserir valor no fim da lista
idade.append(18)
print(idade)

#inserir valor em uma posição especifica da lista
idade.insert(3,44)
print(idade)

#remover a ultima posição da lista
idade.pop()
print(idade)

#remover valor em uma posição especifica da lista
idade.pop(4)
print(idade)

#remover valor declarado
idade.remove(60)
print(idade)

#tamanho da lista
print(len(idade))

#ordenar lista asc
idade.sort()
print(idade)

#ordenar lista desc
idade.sort(reverse=True)
print(idade)

#inverter objetos da lista
idade.reverse()
print(idade)

#Valor maximo e minimo da lista
print(max(idade))
print(min(idade))

#Soma dos valores da lista

print(sum(idade))

#ordenar
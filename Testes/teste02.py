qtdItem = 10
estoque = 50

print('A quantidade de itens é {}, e o total em estoque é {}.'.format(qtdItem, estoque))

# Declarando dessa forma as variaveis no format é possivel inverter a ordem na string
print('A quantidade de estoque é {e}, e o total em itens é {i}.'.format(i=qtdItem, e=estoque))

print(type(estoque))

var1 = 'dasdfasdfasd'
var2 = True

print('var1 é:', type(var1), ', var2 é:', type(var2))

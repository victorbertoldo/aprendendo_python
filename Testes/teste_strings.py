str = 'Victor hugo ROCHA'

#maiusculo
str = str.upper()
print(str)

#minusculo
str = str.lower()
print(str)

# Quantos caracteres tem?
print(len(str))

# Substituir caracter

str = str.replace('rocha','bertoldo')
print(str)

#  Contar caracter dentro de uma string
var = 'cc bb eee fodfd c tifdc'
print(var.count('c'))

#localizar letra
print(var.find('t'))

# Capitalizar uma string (1ª letra maiuscula)
print(str.title())
nome = input('digite seu nome:')
idade = int(input('digite sua idade:'))
n1 = int(input('digite a nota da n1:'))
n2 = int(input('digite a nota da n2:'))

nome = nome.lower().title()
media = (n1+n2)/2

print(f'A média é: {media}')

if media >=6 and idade >=18:
    print(f'Media: {media}. Vc foi aprovado.')
else:
    print(f'Media: {media}, vc não foi aprovado.')


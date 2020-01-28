#x = dict()
x = {'nome' : 'Victor', 'idade' : 31, 'telefone' : '9999999999'}

print(x['nome'])

print(len(x))
x.pop('telefone')

print(len(x))

cadastro = [{'nome' : 'Victor', 'idade' : 31, 'telefone' : '9999999999','cpf': '12345789654'},
            {'nome' : 'Jão', 'idade' : 51, 'telefone' : '9999999999','cpf': '98754561321'}]

print(cadastro[0])
print(cadastro[1]['idade'])
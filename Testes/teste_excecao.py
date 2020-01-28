try:
    x = int(input('Digite sua idade:'))
except: # caso ocorra erro de exceção ira retornar o q está abaixo do except
    print('Idade inválida!')
else: # se não houver falhas irá executar o que está abaixo do else
    print(f'Sua idade é {x}.')
finally: # irá executar de qlqr maneira, retornando falhas ou não
    print('Obrigado!')
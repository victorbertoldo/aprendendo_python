import pymysql.cursors
import matplotlib.pyplot as plt

conexao = pymysql.connect(
    host='localhost',
    port=3308,
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

autenticado = False

def logarCadastrar():
    usuarioExistente = 0
    autenticacao = False
    usuarioMaster = False
    if opcao == 1:
        nome = input('Digite seu nome:')
        senha = input('Digite sua senha:')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] ==2:
                    usuarioMaster = True
                autenticacao = True
                break
            else:
                autenticacao = False


        if not autenticacao:
            print('usuario ou senha invalidos!')
    elif opcao == 2:
        print('Faça seu cadastro')
        nome = input('Digite seu nome:')
        senha = input('Digite sua senha:')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('Usuário já cadastrado na base. Tente novamente.')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s);',(nome, senha, 1))
                    conexao.commit()
                print('Usuario cadastrado com sucesso!')
            except:
                print('Erro ao inserir os dados')
    return autenticacao, usuarioMaster

def cadastrarProdutos():
    nome = input('Digite o nome do produto:')
    ingredientes = input('Digite os ingredientes dos produtos')
    grupo = input('Informe o grupo, o qual o produto pertence:')
    preco = float(input('Digite o preço do produto:'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s,%s,%s,%s)',(nome, ingredientes, grupo, preco))
            conexao.commit()
            print('Produto cadastrado com sucesso!')
    except:
        print('Erro ao inserir produtos no banco de dados')

def listarProdutos():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()
            #print(produtosCadastrados)
    except:
        print('Erro ao conectar ao Banco de Dados!')

    for i in produtosCadastrados:
        produtos.append(i)

    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum produto cadastrado.')

def excluirProdutos():
    idDeletar = int(input('Digite o id referente ao produto que deseja apagar:'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletar))

    except:
        print('Erro ao excluir o produto!')

def listarPedidos():
    pedidos = []
    decision = 0

    while decision !=2:
        pedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listaPedidos = cursor.fetchall()
        except:
            print('Erro no banco de dados!')

        for i in listaPedidos:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('Nenhum pedido foi feito.')

        decision = int(input('Digite 1 para entregar um produto e 2 para voltar.'))

        if decision == 1:
            idDeletar = int(input('Digite o id do pedido entregue'))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print('Produto entregue')
            except:
                print('Erro ao entregar pedido')

def gerarEstatistica():
    nomeProdutos = []
    nomeProdutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except:
        print('Erro ao conectar no banco de dados!')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticavendido')
            vendido = cursor.fetchall()
    except:
        print('Erro ao conectar no banco de dados!')

    estado = int(input('Digite 0 para sair, 1 para pesquisar por nome e 2 para pesquisar por grupo:'))

    if estado == 1:
        decisao3 = int(input('Digite 1 ppara pesquisar por dinheiro e 2 por quantidade unitaria:'))
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append(i['nome'])

            valores = []
            valores.clear()

            for h in range(0,len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['nome'] == nomeProdutos[h]:
                        somaValor += i['preco']

                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor+1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Qtd vendida em reais')
            plt.xlabel('Produtos')
            plt.show()

        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print('erro na consulta')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticavendido')
                    vendidoGrupo = cursor.fetchall()

            except:
                print('erro na consulta')

            for i in grupo:
                grupoUnico.append(i['nome'])

            grupoUnico = sorted(set(grupoUnico))
            qntFinal = []
            qntFinal.clear()

            for h in range(0, len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['nome']:
                        qntUnitaria += 1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico, qntFinal)
            plt.ylabel('Qtd Unitaria vendida')
            plt.xlabel('produtos')
            plt.show()

    elif estado ==2:
        decisao3 = int(input('Digite 1 ppara pesquisar por dinheiro e 2 por quantidade unitaria:'))
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append(i['grupo'])

            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['grupo'] == nomeProdutos[h]:
                        somaValor += i['preco']

                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Qtd vendida em reais')
            plt.xlabel('Produtos')
            plt.show()

        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print('erro na consulta')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticavendido')
                    vendidoGrupo = cursor.fetchall()

            except:
                print('erro na consulta')

            for i in grupo:
                grupoUnico.append(i['grupo'])

            grupoUnico = sorted(set(grupoUnico))
            qntFinal = []
            qntFinal.clear()

            for h in range(0, len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['grupo']:
                        qntUnitaria += 1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico, qntFinal)
            plt.ylabel('Qtd Unitaria vendida')
            plt.xlabel('grupo')
            plt.show()



while not autenticado:
    opcao = int(input('Digite 1 para logar e 2 para cadastrar:'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()

    except:
        print('Erro ao conectar ao banco de dados!')

    autenticado, usuarioSupremo = logarCadastrar()

if autenticado == True:
    print('Autenticado!')


    if usuarioSupremo == True:
        decisaoUsuario = 1

        while decisaoUsuario != 0:
            decisaoUsuario = int(input('Digite 0 para sair, 1 para cadastrar produtos e 2 para listar produtos, 3 para listar os pedidos e 4 para visualizar as estatisticas:'))

            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('Digite 1 para excluir um produto ou 2 para sair:'))

                if delete == 1:
                    excluirProdutos()

            elif decisaoUsuario == 3:
                listarPedidos()
            elif decisaoUsuario == 4:
                gerarEstatistica()

import pymysql.cursors

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
            decisaoUsuario = int(input('Digite 0 para sair, 1 para cadastrar produtos e 2 para listar produtos:'))

            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('Digite 1 para excluir um produto ou 2 para sair:'))

                if delete == 1:
                    excluirProdutos()

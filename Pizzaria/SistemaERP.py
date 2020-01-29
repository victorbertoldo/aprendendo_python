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
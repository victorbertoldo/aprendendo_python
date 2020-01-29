import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    port=3308,
    user='root',
    password='',
    db='cursopython',
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor

)

#x = 'create table pessoas(nome varchar(50),	idade int,	cep varchar(20),	cpf varchar(11)); '
#x = 'drop table pessoas;'
tbcadastro = 'create table tbcadastros(id int primary key auto_increment, nome varchar(50) not null, endereco varchar(300));'

nome = str(input('Digite seu nome:'))
#idade = int(input('Informe a idade:'))
end = str(input('Digite seu endereço:'))

with conexao.cursor() as cursor:
     #cursor.execute(tbcadastro)
     cursor.execute('insert into tbcadastros(nome, endereco) values ("{}","{}");'.format(nome,end))
     conexao.commit()



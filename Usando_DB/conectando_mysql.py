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

x = 'create table pessoas(nome varchar(50),	idade int,	cep varchar(20),	cpf varchar(11)); '
#x = 'drop table pessoas;'

with conexao.cursor() as cursor:
    cursor.execute(x)



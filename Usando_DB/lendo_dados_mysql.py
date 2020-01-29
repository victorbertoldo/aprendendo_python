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
with conexao.cursor() as cursor:
    cursor.execute('select * from tbcadastros')
    result = cursor.fetchall()

#print(result)

for dado in result:
    print(dado['nome'])
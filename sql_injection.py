import pymysql

# Variáveis para acessar o banco de dados
db_user = 'root'
db_password = ''
data_base = 'USERS'

# Testando a conexão com o banco de dados
try:
    conn = pymysql.connect(user=db_user, passwd=db_password, db=data_base)
    cursor = conn.cursor()
except:
    print('Falha na conexão com o banco de dados!')
    exit()

# Realizando a consulta no banco de dados
data = "'injection' or 1=1" # Injeção de SQL
cursor.execute("SELECT * FROM USERS WHERE name=%s" % (data))
result = cursor.fetchall()
conn.commit()

# Exibindo o resultado da pesquisa em várias linhas, se for o caso
for linha in result:
    print(f'{linha}')

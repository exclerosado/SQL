import pymysql
import random

# Variáveis para acessar o banco de dados
db_user = 'root'
db_password = ''
data_base = 'USERS'

# Testando a conexão com o Banco de Dados
try:
    conn = pymysql.connect(user=db_user, passwd=db_password, db=data_base)
    cursor = conn.cursor()
except:
    print('Falha de conexão com o banco de dados!')
    exit()

# Dados e caracteres pre-carregados para gerar os usuários e senhas de forma automática
users = ['Marcos', 'Camila', 'José', 'Beatriz', 'Paula', 'Carlos', 'Lucas', 'Priscila', 'Maria', 'Nelson']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_char = ['!', '@', '#', '$', '%', '&', '*']

# Concatenando os caracteres
all = numbers + lower + upper + special_char

while True:
    print('Deseja cadastrar?')
    option = str(input('(y/n): ')).upper()
    if option == 'Y':
        for i in range(len(users)):
            user = str(users[i])
            # Gerando uma senha aleatória de 16 dígitos a partir dos caracteres concatenados
            rand = random.sample(all, 16)
            passwd = str("".join(rand))
            # Cadastrando os dados
            cursor.executemany("INSERT INTO USERS (name, password) VALUES (%s, %s)", list([(user, passwd)]))
            conn.commit()
        print('Cadastros realizados!')
        print('Saindo...')
        break
    elif option == 'N':
        print('Saindo...')
        break
    elif option != 'Y' or option != 'N':
        print('\nOpção inválida! Tente novamente.')

import mysql.connector

mydb = mysql.connector.connect(
    host='172.21.128.1',
    user='wsl_root',
    passwd = '19983006aB'
)
my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
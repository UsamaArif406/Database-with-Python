import mysql.connector
# 127.0.0.1
db = mysql.connector.connect(
    host= "localhost",
    username= "root",
    password= "Rp20ee406",
)

cursor = db.cursor()

query = "CREATE DATABASE student"
# removeQuery = "DROP DATABASE student"
# cursor.execute(query)
print(db)
selectDB = 'USE student'
cursor.execute(selectDB)
# createTableQuery = '''CREATE TABLE studentDetails (
# id int auto_increment unique,
# name varchar(255) not null,
# age int not null
# )'''

# cursor.execute(createTableQuery)

insertData = '''INSERT INTO studentdetails (name, age) VALUES ('Aun', 20), ('Talha', 22)'''
# cursor.execute(insertData)

# db.commit()

selectData = 'SELECT * FROM studentdetails ORDER BY id DESC'
cursor.execute(selectData)

print ('Student Data', cursor.fetchone())
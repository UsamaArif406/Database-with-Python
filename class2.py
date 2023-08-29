import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username = 'root',
    password = 'Rp20ee406',
    database = 'student'
)

print(db)

query = 'INSERT INTO studentdetails (name, age) VALUES (%s, %s)'
data = [
    ('Sam', 50),
    ('Bushra', 60),
    ('Rayan', 20)
]

cursor = db.cursor()

cursor.executemany(query, data)

db.commit()

print(cursor.rowcount, 'records inserted')

queryCount = 'SELECT COUNT(*) FROM studentdetails'

cursor.execute(queryCount)
result = cursor.fetchone()
print(result)
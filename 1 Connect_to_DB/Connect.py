import mysql.connector as connector

#добавление
db = connector.connect(host = "127.0.0.1", database = "new1", user = "root", password = "")
zapros = "INSERT INTO spisok (Zagolovok, Text) VALUES ('Zagolovok', 'Text statey')"

c = db.cursor()
c.execute(zapros)
db.commit()

#изменение

izmenenie = "UPDATE spisok SET Zagolovok = 'new Zagolovok' WHERE ID = 1"
c = db.cursor()
c.execute(izmenenie)
db.commit()

from Models import db, Professor, Student, Discipline, JoinDS

db.connect()
db.create_tables([Professor, Student, Discipline, JoinDS])
db.close()

print("Tabelele au fost create cu succes!")

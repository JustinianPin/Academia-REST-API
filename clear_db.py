from Models.database import db
from Models.professor import Professor
from Models.student import Student
from Models.discipline import Discipline
from Models.join_ds import JoinDS

def clear_database():
    db.connect()
    db.drop_tables([JoinDS, Discipline, Student, Professor])
    db.close()
    print("Toate tabelele si datele au fost șterse.")

if __name__ == "__main__":
    clear_database()

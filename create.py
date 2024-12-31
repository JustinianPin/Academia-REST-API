from Models.database import db
from Models.professor import Professor
from Models.student import Student
from Models.discipline import Discipline
from Models.join_ds import JoinDS

def create_and_populate():
    db.connect()
    db.create_tables([Professor, Student, Discipline, JoinDS])

    professors = [
        {"nume": "Toma", "prenume": "Ion", "email": "popescu.ion@academic.academia.com", "grad_didactic": "prof", "tip_asociere": "titular", "afiliere": "Universitatea Gh. Asachi Iasi"},
        {"nume": "Petrescu", "prenume": "Maria", "email": "ionescu.maria@academic.academia.com", "grad_didactic": "conf", "tip_asociere": "asociat", "afiliere": "Universitatea Gh. Asachi Iasi"},
    ]
    Professor.insert_many(professors).execute()

    students = [
        {"nume": "Popescu", "prenume": "Elena", "email": "elena.popescu@student.academia.com", "ciclu_studii": "licenta", "an_studiu": 1, "grupa": 101},
        {"nume": "Ionescu", "prenume": "Mihai", "email": "mihai.ionescu@student.academia.com", "ciclu_studii": "licenta", "an_studiu": 2, "grupa": 102},
    ]
    Student.insert_many(students).execute()

    disciplines = [
        {"cod": "SD101", "id_titular": 1, "nume_disciplina": "Structuri de Date", "an_studiu": 1, "tip_disciplina": "impusa", "categorie_disciplina": "specialitate", "tip_examinare": "examen"},
        {"cod": "APD102", "id_titular": 2, "nume_disciplina": "Achizitia si Prelucrarea Datelor", "an_studiu": 2, "tip_disciplina": "optionala", "categorie_disciplina": "domeniu", "tip_examinare": "colocviu"},
    ]
    Discipline.insert_many(disciplines).execute()

    join_ds_entries = [
        {"disciplina": 1, "student": 1},
        {"disciplina": 2, "student": 2},
    ]
    JoinDS.insert_many(join_ds_entries).execute()

    db.close()
    print("Tabelele au fost create si populate!")

if __name__ == "__main__":
    create_and_populate()

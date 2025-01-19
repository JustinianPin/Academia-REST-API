from peewee import Model

def serialize_professor(professor: Model):
    return {
        "id": professor.id,
        "nume": professor.nume,
        "prenume": professor.prenume,
        "email": professor.email,
        "grad_didactic": professor.grad_didactic,
        "tip_asociere": professor.tip_asociere,
        "afiliere": professor.afiliere,
    }

def serialize_discipline(discipline: Model):
    return {
        "id": discipline.id,
        "cod": discipline.cod,
        "id_titular": discipline.id_titular,
        "nume_disciplina": discipline.nume_disciplina,
        "an_studiu": discipline.an_studiu,
        "tip_disciplina": discipline.tip_disciplina,
        "categorie_disciplina": discipline.categorie_disciplina,
        "tip_examinare": discipline.tip_examinare,
    }

def serialize_student(student: Model):
    return {
        "id": student.id,
        "nume": student.nume,
        "prenume": student.prenume,
        "email": student.email,
        "ciclu_studii": student.ciclu_studii,
        "an_studiu": student.an_studiu,
        "grupa": student.grupa,
    }

from peewee import Model, ForeignKeyField
from .database import db
from .discipline import Discipline
from .student import Student

class JoinDS(Model):
    disciplina_id = ForeignKeyField(Discipline, backref="studenti", on_delete="CASCADE")
    student_id = ForeignKeyField(Student, backref="discipline", on_delete="CASCADE")

    class Meta:
        database = db

from peewee import Model, ForeignKeyField
from .database import db
from .discipline import Discipline
from .student import Student

class JoinDS(Model):
    disciplina = ForeignKeyField(Discipline, backref='students')
    student = ForeignKeyField(Student, backref='disciplines')

    class Meta:
        database = db
        table_name = 'join_ds'

from peewee import Model, CharField, IntegerField, AutoField, EnumField, ForeignKeyField
from .database import db
from .professor import Professor

class Discipline(Model):
    id = AutoField()
    id_titular = ForeignKeyField(Professor, backref="discipline", on_delete="CASCADE")
    nume_disciplina = CharField(max_length=200)
    an_studiu = IntegerField()
    tip_disciplina = EnumField(choices=["impusa", "optionala", "liber_aleasa"])
    categorie_disciplina = EnumField(choices=["domeniu", "specialitate", "adiacenta"])
    tip_examinare = EnumField(choices=["examen", "colocviu"])

    class Meta:
        database = db

from peewee import Model, CharField, AutoField, IntegerField
from .database import db

TIP_DISCIPLINA = ["impusa", "optionala", "liber_aleasa"]
CATEGORIE_DISCIPLINA = ["domeniu", "specialitate", "generala"]
TIP_EXAMINARE = ["examen", "colocviu"]

class Discipline(Model):
    id = AutoField()
    cod = CharField(max_length=10, unique=True)
    id_titular = IntegerField()
    nume_disciplina = CharField(max_length=200)
    an_studiu = IntegerField()
    tip_disciplina = CharField(choices=TIP_DISCIPLINA, max_length=20)
    categorie_disciplina = CharField(choices=CATEGORIE_DISCIPLINA, max_length=20)
    tip_examinare = CharField(choices=TIP_EXAMINARE, max_length=20)

    class Meta:
        database = db
        table_name = 'disciplines'

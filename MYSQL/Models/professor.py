from peewee import Model, CharField, AutoField
from .database import db

GRAD_DIDACTIC = ["prof", "conf", "asist"]
TIP_ASOCIERE = ["titular", "asociat", "extern"]

class Professor(Model):
    id = AutoField()
    nume = CharField(max_length=100)
    prenume = CharField(max_length=100)
    email = CharField(max_length=150)
    grad_didactic = CharField(choices=GRAD_DIDACTIC, max_length=10)
    tip_asociere = CharField(choices=TIP_ASOCIERE, max_length=10)
    afiliere = CharField(max_length=200)

    class Meta:
        database = db
        table_name = 'professors'

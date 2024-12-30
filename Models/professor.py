from peewee import Model, CharField, AutoField, EnumField
from .database import db

class Professor(Model):
    id = AutoField()
    nume = CharField(max_length=100)
    prenume = CharField(max_length=100)
    email = CharField(max_length=150, unique=True)
    grad_didactic = EnumField(choices=["asist", "sef lucr", "conf", "prof"], null=True)
    tip_asociere = EnumField(choices=["titular", "asociat", "extern"], null=False)
    afiliere = CharField(max_length=200, default='Universitatea "Gh. Asachi" Iasi')

    class Meta:
        database = db

from peewee import Model, CharField, AutoField, IntegerField
from .database import db

CICLU_STUDII = ["licenta", "master", "doctorat"]

class Student(Model):
    id = AutoField()
    nume = CharField(max_length=100)
    prenume = CharField(max_length=100)
    email = CharField(max_length=150)
    ciclu_studii = CharField(choices=CICLU_STUDII, max_length=20)
    an_studiu = IntegerField()
    grupa = IntegerField()

    class Meta:
        database = db
        table_name = 'students'

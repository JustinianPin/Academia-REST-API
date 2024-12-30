from peewee import Model, CharField, IntegerField, AutoField, EnumField
from .database import db

class Student(Model):
    id = AutoField()
    nume = CharField(max_length=100)
    prenume = CharField(max_length=100)
    email = CharField(max_length=150, unique=True)
    ciclu_studii = EnumField(choices=["licenta", "master"], null=False)
    an_studiu = IntegerField()
    grupa = IntegerField()

    class Meta:
        database = db

from peewee import MySQLDatabase
from decouple import config

db = MySQLDatabase(
    config("MARIADB_DATABASE"),
    user=config("MARIADB_USER"),
    password=config("MARIADB_PASSWORD"),
    host=config("MARIADB_HOST"),
    port=int(config("MARIADB_PORT")),
)

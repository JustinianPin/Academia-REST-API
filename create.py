import os
from sqlite3 import OperationalError
from peewee import MySQLDatabase

db = MySQLDatabase(
    database="academia",
    user="pos_admin",
    password="parola",
    host="localhost",
    port=3306,
)

try:
    with db.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS academia;")
        cursor.execute("USE academia;")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PROFESORI (
                ID INT(3) AUTO_INCREMENT PRIMARY KEY,
                nume VARCHAR(100) NOT NULL,
                prenume VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE,
                grad_didactic ENUM('asist', 'sef lucr', 'conf', 'prof') NULL,
                tip_asociere ENUM('titular', 'asociat', 'extern') NOT NULL,
                afiliere VARCHAR(200) NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS STUDENTI (
                ID INT(3) AUTO_INCREMENT PRIMARY KEY,
                nume VARCHAR(100) NOT NULL,
                prenume VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE,
                ciclu_studii ENUM('licenta', 'master') NOT NULL,
                an_studiu INT NOT NULL,
                grupa INT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS DISCIPLINE (
                COD INT(3) PRIMARY KEY,
                ID_titular INT(3) NOT NULL,
                nume_disciplina VARCHAR(200) NOT NULL,
                an_studiu INT NOT NULL,
                tip_disciplina ENUM('impusa', 'optionala', 'liber_aleasa') NOT NULL,
                categorie_disciplina ENUM('domeniu', 'specialitate', 'adiacenta') NOT NULL,
                tip_examinare ENUM('examen', 'colocviu') NOT NULL,
                FOREIGN KEY (ID_titular) REFERENCES PROFESORI(ID) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS JOIN_DS (
                DisciplinaID INT(3),
                StudentID INT(3),
                PRIMARY KEY (DisciplinaID, StudentID),
                FOREIGN KEY (DisciplinaID) REFERENCES DISCIPLINE(COD) ON DELETE CASCADE,
                FOREIGN KEY (StudentID) REFERENCES STUDENTI(ID) ON DELETE CASCADE
            );
        """)

        # Actualizăm adresele de e-mail și afilierea
        cursor.execute("""
            INSERT IGNORE INTO PROFESORI (nume, prenume, email, grad_didactic, tip_asociere, afiliere)
            VALUES 
                ('Popescu', 'Ion', 'popescu.ion@academic.academia.com', 'prof', 'titular', 'Universitatea "Gh. Asachi" Iasi'),
                ('Ionescu', 'Maria', 'ionescu.maria@academic.academia.com', 'conf', 'asociat', 'Universitatea "Gh. Asachi" Iasi'),
                ('Vasilescu', 'Andrei', 'vasilescu.andrei@academic.academia.com', 'asist', 'extern', 'Universitatea "Gh. Asachi" Iasi');
        """)

        cursor.execute("""
            INSERT IGNORE INTO STUDENTI (ID, nume, prenume, email, ciclu_studii, an_studiu, grupa)
            VALUES 
                (101, 'Popescu', 'Elena', 'elena.popescu@student.academia.com', 'licenta', 1, 101),
                (102, 'Ionescu', 'Mihai', 'mihai.ionescu@student.academia.com', 'licenta', 2, 102),
                (103, 'Dumitrescu', 'Ioana', 'ioana.dumitrescu@student.academia.com', 'master', 1, 201);
        """)

        cursor.execute("""
            INSERT IGNORE INTO DISCIPLINE (COD, ID_titular, nume_disciplina, an_studiu, tip_disciplina, categorie_disciplina, tip_examinare)
            VALUES 
                (201, 1, 'Matematica', 1, 'impusa', 'domeniu', 'examen'),
                (202, 1, 'Informatica', 1, 'optionala', 'specialitate', 'colocviu'),
                (203, 2, 'Fizica', 2, 'impusa', 'adiacenta', 'examen');
        """)

        cursor.execute("""
            INSERT IGNORE INTO JOIN_DS (DisciplinaID, StudentID)
            VALUES 
                (201, 101), 
                (202, 102),
                (203, 103);
        """)

        db.commit()
        print("Database setup completed successfully!")

except OperationalError as e:
    print(f"Error: {e}")

finally:
    db.close()

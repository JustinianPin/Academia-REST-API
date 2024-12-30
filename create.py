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
                ID INT AUTO_INCREMENT PRIMARY KEY,
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
                ID INT AUTO_INCREMENT PRIMARY KEY,
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
                COD VARCHAR(20) PRIMARY KEY,
                ID_titular INT NOT NULL,
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
                DisciplinaID VARCHAR(20),
                StudentID INT,
                PRIMARY KEY (DisciplinaID, StudentID),
                FOREIGN KEY (DisciplinaID) REFERENCES DISCIPLINE(COD) ON DELETE CASCADE,
                FOREIGN KEY (StudentID) REFERENCES STUDENTI(ID) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            INSERT IGNORE INTO PROFESORI (nume, prenume, email, grad_didactic, tip_asociere, afiliere)
            VALUES 
                ('Popescu', 'Ion', 'popescu.ion@example.com', 'prof', 'titular', 'Universitatea X'),
                ('Ionescu', 'Maria', 'ionescu.maria@example.com', 'conf', 'asociat', 'Universitatea Y'),
                ('Vasilescu', 'Andrei', 'vasilescu.andrei@example.com', 'asist', 'extern', 'Institutul Z');
        """)

        cursor.execute("""
            INSERT IGNORE INTO STUDENTI (nume, prenume, email, ciclu_studii, an_studiu, grupa)
            VALUES 
                ('Popescu', 'Elena', 'elena.popescu@example.com', 'licenta', 1, 101),
                ('Ionescu', 'Mihai', 'mihai.ionescu@example.com', 'licenta', 2, 102),
                ('Dumitrescu', 'Ioana', 'ioana.dumitrescu@example.com', 'master', 1, 201);
        """)

        cursor.execute("""
            INSERT IGNORE INTO DISCIPLINE (COD, ID_titular, nume_disciplina, an_studiu, tip_disciplina, categorie_disciplina, tip_examinare)
            VALUES 
                ('MATH101', 1, 'Matematica', 1, 'impusa', 'domeniu', 'examen'),
                ('INF102', 1, 'Informatica', 1, 'optionala', 'specialitate', 'colocviu'),
                ('PHY201', 2, 'Fizica', 2, 'impusa', 'adiacenta', 'examen');
        """)

        cursor.execute("""
            INSERT IGNORE INTO JOIN_DS (DisciplinaID, StudentID)
            VALUES 
                ('MATH101', 1), 
                ('INF102', 2),
                ('PHY201', 3);
        """)

        db.commit()
        print("Database setup completed successfully!")

except OperationalError as e:
    print(f"Error: {e}")

finally:
    db.close()

# Academia-REST-API

**Backend and Database project for managing an academic environment**

---

## Description

This repository contains the backend implementation of an academic management system. The project is structured as a RESTful API using Python, with both relational and non-relational database integration. It is designed following the **Model-View-Controller (MVC)** architectural pattern, and uses **Docker** for containerization and **Postman** for testing endpoints.

> The full commit history of the project can be found in the branch **`project`**.

---

## Functionality

The core features of the application include:
- Management of **students**, **professors**, and **courses**
- Relational and non-relational data handling
- Endpoint testing

Most functionalities are demonstrated through **Postman screenshots**, available in the `Demonstrative logs` folder.

---

## Technical Overview

### Backend
- Implemented in **Python**, following the **MVC** structure:
  - `Controllers/` – route handling and business logic interface
  - `Models/` – ORM models for data entities
  - `Services/` – logic encapsulation for database interactions

### Relational Database
- Located in the `MariaDB/` folder
- Uses **MariaDB** and **Peewee ORM**
- Models:
  - `student.py` – student entities
  - `discipline.py` – course entities
  - `professor.py` – teaching staff
  - `join_ds.py` – many-to-many relationship between students and disciplines:
    ```python
    class JoinDS(Model):
        disciplina = ForeignKeyField(Discipline, backref='students')
        student = ForeignKeyField(Student, backref='disciplines')
    ```

### NoSQL Integration
- **MongoDB** is used to manage course-related content
- Implemented under `MongoDB/discipline.py`, also following MVC pattern

### Testing
- API endpoints are tested using **Postman**
- Test evidence is provided in the `Demonstrative logs/` folder

### Containerization
- **Docker** is used for environment setup
- A `docker-compose.yml` file is provided for orchestrating services

---

## Frontend

A frontend implementation is **not yet included**, as the focus was on backend architecture and database integration.

---

## Technologies Used

- Python
- Peewee ORM
- MariaDB
- MongoDB
- Docker & Docker Compose
- Postman

---

## Final Notes

This project is part of a personal academic initiative and was developed with clean code practices, modular design, and scalability in mind. It demonstrates my ability to structure backend systems using Python and to work with both SQL and NoSQL databases in a containerized environment.

---

## Author

Justinian Pintilie





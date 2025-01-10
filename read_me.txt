LA INCEPUT:

1. Run:
 docker-compose up -d 
2. Creaaza BD in DBeaver
3. python create.py

sau cu un docker deja creat, rulezi python clear_db.py ca sa nu mai faci o noua DB in DBeaver.


RULARE: 
1. Pornesc cointainerul Docker pentru Academia (cu portul 3306)
2. Conectare si verificare din DBeaver
3. din VS Code, rulam proiectul cu comanda: python -m uvicorn main:app --reload 


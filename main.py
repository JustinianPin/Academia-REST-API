from fastapi import FastAPI
from Controllers.professor_controller import router as professor_router
import logging

# Inițializare aplicație FastAPI
app = FastAPI()

# Configurare logging pentru a urmări aplicația
logging.basicConfig(level=logging.INFO)

@app.on_event("startup")
async def startup_event():
    logging.info("Aplicația a pornit corect!")
    logging.info("Rutele înregistrate:")
    for route in app.router.routes:
        logging.info(f"Path: {route.path}, Methods: {route.methods}")

# Înregistrarea router-ului pentru profesori
app.include_router(professor_router, prefix="/api/academia", tags=["Professors"])

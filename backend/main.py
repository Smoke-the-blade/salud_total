from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS para permitir acceso desde React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambiar si usás otro puerto en Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensaje": "API de Salud Total en FastAPI está funcionando"}
from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS para permitir acceso desde React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Cambiar si usás otro puerto en Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción poné solo la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulamos una base de datos con 1 usuario por ahora
FAKE_ADMIN_DB = {
    "admin@clinica.com": {
        "contrasena": "admin123",  # en producción, usar hash (ej. bcrypt)
    }
}

@app.post("/login")
def login(email: str = Form(...), contrasena: str = Form(...)):
    usuario = FAKE_ADMIN_DB.get(email)
    if not usuario or usuario["contrasena"] != contrasena:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"mensaje": "Login exitoso", "usuario": email}
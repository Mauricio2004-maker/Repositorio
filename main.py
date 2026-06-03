from fastapi import FastAPI

app = FastAPI()

usuarios = []

# Crear
@app.post("/usuarios")
def crear(usuario: dict):
    usuarios.append(usuario)
    return usuario

# Leer
@app.get("/usuarios")
def listar():
    return usuarios

# Actualizar
@app.put("/usuarios/{id}")
def actualizar(id: int, usuario: dict):
    usuarios[id] = usuario
    return usuario

# Eliminar
@app.delete("/usuarios/{id}")
def eliminar(id: int):
    eliminado = usuarios.pop(id)
    return eliminado
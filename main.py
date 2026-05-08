from fastapi import FastAPI

app = FastAPI()

# Base de datos falsa
users = []

# CREATE
@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return {"message": "Usuario creado", "data": user}

# READ
@app.get("/users")
def get_users():
    return users

# UPDATE
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    users[user_id] = user
    return {"message": "Usuario actualizado", "data": user}

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = users.pop(user_id)
    return {"message": "Usuario eliminado", "data": deleted}
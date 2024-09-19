from fastapi import FastAPI, HTTPException

app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
def get_users():
    return users_db


@app.post("/user/{username}/{age}")
def add_user(username: str, age: int):
    if not username or age <= 0:
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или возраст")

    current_id = str(max(int(k) for k in users_db.keys()) + 1)
    users_db[current_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"User {current_id} is registered"}


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if not username or age <= 0:
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или возраст")

    users_db[user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"User {user_id} has been updated"}


@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users_db[user_id]
    return {"message": f"User {user_id} has been deleted"}
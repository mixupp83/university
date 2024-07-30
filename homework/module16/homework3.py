from fastapi import FastAPI, HTTPException

app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    return users_db

@app.post("/user/{username}/{age}")
def add_user(username: str, age: int):
    current_id = str(int(max(users_db, key=int)) + 1)
    users_db[current_id] = username, age
    return f"User {username} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return f"User {user_id} is deleted"
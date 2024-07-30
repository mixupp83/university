from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
def admin_page():
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
def user_page(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get('/user')
def user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

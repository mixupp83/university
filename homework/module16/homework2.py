from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
def main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
def admin_page():
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
def user_page(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]):
    return {"message": f"Вы вощли как пользователь № {user_id}"}


@app.get('/user')
def user_info(username: Annotated[str, Path(min_length=5, max_length=18, description='Enter Username')],
              age: Annotated[int, Path(ge=18, le=120, description="Enter возраст")]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

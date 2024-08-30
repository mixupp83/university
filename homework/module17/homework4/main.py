from fastapi import FastAPI
from task import router as task_router
from user import router as user_router
from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
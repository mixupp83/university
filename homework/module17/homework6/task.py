from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import select, insert, update, delete
from slugify import slugify

router = APIRouter(
    prefix="/task",
    tags=["task"]
)


@router.get("/")
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/{task_id}")
def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    slug = slugify(task.title)

    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id,
        slug=slug
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    for key, value in task.dict().items():
        setattr(existing_task, key, value)

    db.commit()
    db.refresh(existing_task)

    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


@router.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.delete(existing_task)
    db.commit()

    return {"status_code": status.HTTP_200_OK, "transaction": "Task delete is successful!"}

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User, Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import select, insert, update, delete
from slugify import slugify

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/")
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/{user_id}")
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(user.username)
    existing_user = db.scalar(select(User).where(User.slug == slug))
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slug
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    for key, value in user.dict().items():
        setattr(existing_user, key, value)

    db.commit()
    db.refresh(existing_user)

    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    for task in tasks:
        db.delete(task)

    db.delete(existing_user)
    db.commit()

    return {"status_code": status.HTTP_200_OK, "transaction": "User delete is successful!"}


@router.get("/{user_id}/tasks")
def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks
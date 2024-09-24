from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from backend.models import User
from backend.schemas import CreateUser, UpdateUser, UserResponse
from sqlalchemy import select, update, delete
from slugify import Slugify
from backend.db_depends import get_db

router = APIRouter()

slugify = Slugify()


@router.get("/", response_model=list[UserResponse])
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/{user_id}", response_model=UserResponse)
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(user.username)
    db_user = User(
        username=user.username,
        firstname=user.firstname,
        secondname=user.secondname,
        age=user.age,
        slug=slug
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    db_user = db.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    for var, value in vars(user).items():
        if value is not None:
            setattr(db_user, var, value)

    if user.username is not None:
        db_user.slug = slugify(user.username)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    db_user = db.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.delete(db_user)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User delete is successful!"}
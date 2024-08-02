from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from lessons.module17.lesson1.backend.db_depends import get_db
from typing import Annotated

from lessons.module17.lesson1.models import *
from sqlalchemy import insert
from lessons.module17.lesson1.schemas import CreateCategory

from slugify import slugify

router = APIRouter(prefix="/category", tags=["category"])

@router.get("/all_categoies")
async def get_all_categories(db: Annotated[Session,Depends(get_db)], create_category: CreateCategory):
    db.execute(insert(Category).values(name=create_category.name, parent_id=create_category.parent_id, slug=slugify(create_category.name)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

#---------------------------
from sqlalchemy import select

@router.get('/all_catigories')
async def get_all_categories(db: Annotated[Session, Depends(get_db)]):
    categories = db.scalars(select(Category).where(Category.is_active == True)).all()
    return categories

@router.put("/update_category")
async def update_category(db: Annotated[Session, Depends(get_db)], category_id: int, update_category: CreateCategory):
    category = db.scalars(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no category found')
    db.execute(update(Category).where(Category.id == category_id).values(name=update_category.name, slug=slugify(update_category.name),parent_id=update_category.parent_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'category update is successful'}



@router.delete("/delete")
async def delete_category():
    pass

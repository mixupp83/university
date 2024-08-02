from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from lessons.module17.lesson1.backend.db_depends import get_db
from typing import Annotated

from lessons.module17.lesson1.models import *
from sqlalchemy import insert
from lessons.module17.lesson1.schemas import CreateCategory, CreateProduct

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update

router = APIRouter(prefix='/products', tags=['products'])

@router.get('/')
async def all_products(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Product).where(Product.is_active == True, Product.stock > 0)).all()
    if products is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no product')
    db.execute(update(Product).where(Product.id == product_id).values(is_active=False))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Product delete is successful'}
from fastapi import FastAPI
from lessons.module17.lesson1.routers import category, products


app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My shop"}

app.include_router(category.router)
app.include_router(products.router)


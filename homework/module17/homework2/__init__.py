from sqlalchemy.schema import CreateTable
from homework.module17.homework2.backend.db import engine, Base
from homework.module17.homework2.models import User, Task

# Создаем таблицы и выводим SQL запрос
Base.metadata.create_all(bind=engine)

print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))
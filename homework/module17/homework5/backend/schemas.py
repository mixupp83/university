from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    secondname: str
    age: int

class UpdateUser(BaseModel):
    username: str | None = None
    firstname: str | None = None
    secondname: str | None = None
    age: int | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    secondname: str
    age: int
    slug: str

    class Config:
        from_attributes = True
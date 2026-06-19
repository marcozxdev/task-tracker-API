from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    email: str


class UserValidation(BaseModel):
    email: str
    password: str

class UserCreate(User):
    password: str


class UserResponse(User):
    id: int


class Task(BaseModel):
    titulo: str
    descripcion: str
    estado: str


class TaskCreate(Task):
    user_id: int


class TaskResponse(TaskCreate):
    id: int













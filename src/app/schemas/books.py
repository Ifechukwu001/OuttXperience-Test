from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

    class Config:
        orm_mode = True

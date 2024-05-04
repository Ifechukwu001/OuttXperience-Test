from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    author: str
    year: int
    isbn: str


class Book(BaseBook):
    pass


class BookRetrieve(BaseBook):
    id: int

    class ConfigDict:
        from_attributes = True

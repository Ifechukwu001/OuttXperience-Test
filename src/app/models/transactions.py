from sqlalchemy.orm import Session

from .books import Book
from ..schemas import books as schemas


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).get(book_id)


def create_book(db: Session, book: schemas.Book):
    book_object = Book(**book.model_dump())
    db.add(book_object)
    db.commit()
    db.refresh(book_object)
    return book_object


def update_book(db: Session, book_id: int, book: schemas.Book):
    book_object = db.query(Book).get(book_id)
    book_object.update(**book.model_dump())  # type: ignore
    db.commit()
    db.refresh(book_object)
    return book_object


def delete_book(db: Session, book_id: int):
    book_object = db.query(Book).get(book_id)
    if book_object:
        db.delete(book_object)
        db.commit()
        return True

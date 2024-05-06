from sqlalchemy.orm import Session

from .books import Book
from ..schemas import books as schemas


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: schemas.Book):
    book_object = Book(**book.model_dump())
    db.add(book_object)
    db.commit()
    db.refresh(book_object)
    return book_object


def update_book(db: Session, book_id: int, book: schemas.Book):
    book_object = db.query(Book).filter(Book.id == book_id).first()
    if book_object:
        for key, value in book.model_dump().items():
            setattr(book_object, key, value)
        db.commit()
        db.refresh(book_object)
        return book_object


def delete_book(db: Session, book_id: int):
    book_object = db.query(Book).get(book_id)
    if book_object:
        db.delete(book_object)
        db.commit()
        return True

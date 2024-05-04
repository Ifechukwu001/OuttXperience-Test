from fastapi import Depends, routing, HTTPException
from sqlalchemy.orm import Session

from ..schemas import books
from ..dependencies import get_db
from ..models import transactions

router = routing.APIRouter()


@router.get("/books/", response_model=list[books.Book])
def get_books(db: Session = Depends(get_db)):
    books = transactions.get_books(db)
    return books


@router.get("/books/{id}", response_model=books.Book)
def get_book(id: int, db: Session = Depends(get_db)):
    book = transactions.get_book(db, id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/books/", response_model=books.Book, status_code=201)
def create_book(book_data: books.Book, db: Session = Depends(get_db)):
    book = transactions.create_book(db, book_data)
    return book


@router.put("/books/{id}", response_model=books.Book)
def update_book(id: int, book_data: books.Book, db: Session = Depends(get_db)):
    book = transactions.update_book(db, id, book_data)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    success = transactions.delete_book(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

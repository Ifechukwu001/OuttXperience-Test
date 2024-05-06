from fastapi.testclient import TestClient

from app.main import app
from app.models.database import Base, testengine
from app.dependencies import get_db, get_test_db

Base.metadata.create_all(bind=testengine)

app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "9780743273565",
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["title"] == "The Great Gatsby"
    assert data["author"] == "F. Scott Fitzgerald"
    assert data["year"] == 1925
    assert data["isbn"] == "9780743273565"


def test_books_id_autoincrement():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "9780743273565",
        },
    )

    data = response.json()

    response2 = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "9780743273565",
        },
    )

    data2 = response2.json()

    response3 = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "9780743273565",
        },
    )

    data3 = response3.json()

    assert data2["id"] - data["id"] == 1
    assert data3["id"] - data2["id"] == 1
    assert data3["id"] - data["id"] == 2


def test_create_validation_empty():
    response = client.post(
        "/books/",
        json={},
    )
    assert response.status_code == 422, response.text


def test_create_validation_missing_title():
    response = client.post(
        "/books/",
        json={
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "9780743273565",
        },
    )
    assert response.status_code == 422, response.text


def test_create_validation_missing_author():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "year": 1925,
            "isbn": "9780743273565",
        },
    )
    assert response.status_code == 422, response.text


def test_create_validation_missing_year():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "9780743273565",
        },
    )
    assert response.status_code == 422, response.text


def test_create_validation_missing_isbn():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
        },
    )
    assert response.status_code == 422, response.text


def test_create_validation_year_cant_parse_int():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925.4,
            "isbn": "9780743273565",
        },
    )
    assert response.status_code == 422, response.text

    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": "year",
            "isbn": "9780743273565",
        },
    )
    assert response.status_code == 422, response.text


def test_validation_isbn_cant_parse_str():
    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": 1234,
        },
    )

    assert response.status_code == 422

    response = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": 1234.23,
        },
    )

    assert response.status_code == 422


def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200, response.text


def test_get_a_book():
    book_id = 1
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200, response.text


def test_get_a_book_not_found():
    book_id = 100
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404, response.text


def test_update_a_book():
    book_id = 1
    response = client.put(
        f"/books/{book_id}",
        json={
            "title": "Unbroken",
            "author": "David Goggins",
            "year": 1900,
            "isbn": "9780746548451",
        },
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Unbroken"
    assert data["author"] == "David Goggins"
    assert data["year"] == 1900
    assert data["isbn"] == "9780746548451"


def test_update_a_book_not_found():
    book_id = 100
    response = client.put(
        f"/books/{book_id}",
        json={
            "title": "Unbroken",
            "author": "David Goggins",
            "year": 1900,
            "isbn": "9780746548451",
        },
    )

    assert response.status_code == 404, response.text


def test_delete_a_book():
    book_id = 1
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == {"message": "Book deleted successfully"}

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404, response.text

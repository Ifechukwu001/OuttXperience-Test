from fastapi import FastAPI

from .routers import books
from .models.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books.router)


@app.get("/")
def home():
    return {"message": "Hello, World!"}

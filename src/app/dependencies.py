from .models.database import SessionLocal, TestSessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

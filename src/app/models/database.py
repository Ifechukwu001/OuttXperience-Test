from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.sqlite3"

TESTSQLALCHEMY_DATABASE_URL = "sqlite:///./test_app.sqlite3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

testengine = create_engine(
    TESTSQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=testengine)


Base = declarative_base()

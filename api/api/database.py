from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.settings import settings

engine = create_engine(settings.pg_dsn)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# ApacheBench Test #1
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

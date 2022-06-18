from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import api.crud as crud
import api.schemas as schemas
from api.database import Base, SessionLocal, engine

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# ApacheBench Test #3
@app.get("/items", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100):
    with SessionLocal() as db:
        items = crud.get_items(db, skip=skip, limit=limit)
        return items

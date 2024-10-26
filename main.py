from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud, database, schemas

app = FastAPI()


def get_db_session() -> Session:
    db_session = database.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.get("/")
def root():
    """Welcome screen"""
    return {"message": "Welcome to FastAPI library manager"}


@app.get("/authors/", response_model=list[schemas.AuthorInfo])
def read_authors(db_session: Session = Depends(get_db_session)):
    """List of authors"""
    return crud.get_all_authors(db_session=db_session)


@app.post("/authors/", response_model=schemas.AuthorInfo)
def create_author(
    author: schemas.AuthorCreate, db_session: Session = Depends(get_db_session)
):
    return crud.create_author(db_session=db_session, author=author)

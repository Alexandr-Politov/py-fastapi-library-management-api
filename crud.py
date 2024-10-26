from sqlalchemy.orm import Session

import models, schemas


def get_all_authors(db_session: Session):
    authors = db_session.query(models.Author).all()
    return authors


def create_author(db_session: Session, author: schemas.AuthorCreate):
    db_new_author = models.Author(name=author.name, bio=author.bio)
    db_session.add(db_new_author)
    db_session.commit()
    db_session.refresh(db_new_author)
    return db_new_author

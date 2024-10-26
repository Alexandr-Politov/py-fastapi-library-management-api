from datetime import date
from pydantic import BaseModel
from typing import ForwardRef, List, Optional


BookAuthorInfo = ForwardRef("AuthorInfo")


class BookBase(BaseModel):
    title: str
    summary: Optional[str] = None
    publication_date: date


class BookCreate(BookBase):
    pass


class BookInfo(BookBase):
    id: int
    author: BookAuthorInfo

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorInfo(BaseModel):
    id: int
    books: List[BookInfo] = []

    class Config:
        orm_mode = True


BookInfo.update_forward_refs()

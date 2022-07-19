from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Book(BaseModel):
    name: str = Field(min_length=1)
    house_no : str = Field(min_length=1, max_length=100)
    street_name : str = Field(min_length=1, max_length=100)
    city: str = Field(min_length=1, max_length=100)
    state : str = Field(min_length=1, max_length=100)
    pincode : int = Field()
    country: str = Field(min_length=1, max_length=100)
    latt : float = Field()
    long : float = Field()

BOOKS = []


@app.post("/mainapp")
def create_address(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.name = book.name
    book_model.house_no = book.house_no
    book_model.street_name = book.street_name
    book_model.city = book.city
    book_model.state = book.state
    book_model.pincode = book.pincode
    book_model.country = book.country
    book_model.latt = book.latt
    book_model.long = book.long


    db.add(book_model)
    db.commit()
    return book

@app.get("/mainapp/{book_id}")
def read_api(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Books).filter(models.Books.id == book_id).first()



@app.put("/mainapp/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )

    book_model.name = book.name
    book_model.house_no = book.house_no
    book_model.street_name = book.street_name
    book_model.city = book.city
    book_model.state = book.state
    book_model.pincode = book.pincode
    book_model.country = book.country
    book_model.latt = book.latt
    book_model.long = book.long

    db.add(book_model)
    db.commit()

    return book


@app.delete("/mainapp/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )

    db.query(models.Books).filter(models.Books.id == book_id).delete()

    db.commit()
from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books=[
{   "id":1,
    "title":"English",
    "pub":"NCERT",
    "price":200
},
{   "id":2,
    "title":"Math",
    "pub":"CBSC",
    "price":2040
},
{   "id":3,
    "title":"Hindi",
    "pub":"Bharti",
    "price":280
},
{   "id":1,
    "title":"Science",
    "pub":"MDH",
    "price":900
}
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Book Not Found")       
        

class Book(BaseModel):
    id:int
    title:str
    pub:str
    price:float


@app.post("/addbooks")
def create_book(book:Book):
    new_book =book.model_dump()
    books.append(new_book)


class BookUpdate(BaseModel):
    title: str
    pub:str
    price:float


@app.put("/book/{book_id}")
def update_book(book_id:int,book_update:BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['pub'] =   book_update.pub
            book['price'] = book_update.price
        return book

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Book Not Found") 

@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book['id'] ==book_id:
            books.remove(book)
            return {"message":"Book is deleted"}

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Book Not Found")        





from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"Message":"Hello World Rocky"}

@app.get("/about")
def about():
    return {"mesaage":"About us content"}


@app.get("/product/{pro_name}")
def get_product_name(pro_name: str,price: Optional[int]=None):
    return {"message": f"product Name is {pro_name} price is {price}"}




class Student(BaseModel):
    name:str
    age:int
    roll:int

@app.post("/create_student")
def create_student(student:Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll":student.roll
    }


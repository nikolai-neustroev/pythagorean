from fastapi import FastAPI
from pydantic import BaseModel

from pythagorean_theorem import hypotenuse


class Request(BaseModel):
    a: int
    b: int


app = FastAPI()

@app.post("/hypotenuse")
def calculate_hypotenuse(request: Request):
    a = request.a
    b = request.b
    c = hypotenuse(a, b)
    return {"c": c}

import logging

from fastapi import FastAPI
from pydantic import BaseModel

from src.pythagorean_theorem import hypotenuse


class Request(BaseModel):
    a: float
    b: float


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

app = FastAPI()


@app.post("/hypotenuse")
def calculate_hypotenuse(request: Request):
    logging.info("Received request to calculate hypotenuse.")
    try:
        a = request.a
        b = request.b
        c = hypotenuse(a, b)
        logging.INFO("Calculated c = %d", c)
        return {"c": c}
    except Exception as e:
        logging.exception("Error calculating hypotenuse: %s", e)
        return {"error": str(e)}

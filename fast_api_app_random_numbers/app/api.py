from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from .utils import generate_random_vector

router = APIRouter()

class Preqin_testing_numbers(BaseModel):
    preqin_testing_numbers: str

@router.post("/random_vector/", response_model=List[float])
async def get_random_vector(input_data: Preqin_testing_numbers):
    try:
        vector = generate_random_vector(500)
        return vector
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd

router = APIRouter()

class PredictRequest(BaseModel):
    feature1: float
    feature2: float

class PredictResponse(BaseModel):
    prediction: float

@router.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    # Replace with your model prediction logic
    df = pd.DataFrame([data.dict()])
    prediction = 0.0  # Dummy prediction
    return PredictResponse(prediction=prediction)

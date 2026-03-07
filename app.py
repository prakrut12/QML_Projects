from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request structure
class Transaction(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Quantum Fraud Detection API running"}

@app.post("/predict")
def predict(transaction: Transaction):

    data = np.array(transaction.features)

    value = np.mean(data)

    if value > 0.5:
        return {"prediction": "Fraud Transaction"}
    else:
        return {"prediction": "Normal Transaction"}

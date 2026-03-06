from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# Allow frontend (Lovable) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Quantum Fraud Detection API running"}

@app.post("/predict")
def predict(data: list):

    value = np.mean(data)

    if value > 0.5:
        return {"prediction": "Fraud Transaction"}
    else:
        return {"prediction": "Normal Transaction"}

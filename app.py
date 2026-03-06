from fastapi import FastAPI
import numpy as np

app = FastAPI()

# Simple fraud prediction placeholder
# Later you can integrate your quantum model here

@app.get("/")
def home():
    return {"message": "Quantum Fraud Detection API running"}

@app.post("/predict")
def predict(data: list):

    # Example logic
    # Replace with your quantum model later
    value = np.mean(data)

    if value > 0.5:
        return {"prediction": "Fraud Transaction"}
    else:
        return {"prediction": "Normal Transaction"}

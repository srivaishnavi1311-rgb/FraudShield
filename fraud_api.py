
from fastapi import FastAPI
from pydantic import BaseModel, Field, StrictBool
import pandas as pd
import joblib

# Create the API application
app = FastAPI(
    title="FraudShield API",
    description="A local transaction risk prediction API",
    version="1.0.0"
)

# Load the improved model
model = joblib.load("fraudshield_improved_model.joblib")


# Define the incoming transaction format
class TransactionRequest(BaseModel):
    amount: float = Field(ge=0)
    international: StrictBool


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to FraudShield API!",
        "status": "running"
    }


# Prediction endpoint
@app.post("/predict")
def predict_transaction(transaction: TransactionRequest):

    # Convert request into model features
    international_number = (
        1 if transaction.international else 0
    )

    features = pd.DataFrame({
        "amount": [transaction.amount],
        "international_number": [international_number]
    })

    # Predict transaction risk
    prediction = int(model.predict(features)[0])

    if prediction == 1:
        status = "SUSPICIOUS"
    else:
        status = "LOW RISK"

    # Return the prediction as JSON
    return {
        "amount": transaction.amount,
        "international": transaction.international,
        "prediction": status
    }

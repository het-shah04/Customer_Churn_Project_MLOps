from fastapi import fastapi
from pydantic import BaseModel
import gradio as gr
from src.serving.inference import predict

app = FastAPI(
    title = "Telco Customer Churn Prediction API",
    description = "ML API for predicting customer churn in telecom industry",
    version = "1.0.0"
)

@app.get("/")
def root():
    """Health check endpoint for monitoring and load balancer health checks"""
    return {"status": "ok"}

class CustomerData(BaseModel):
    """Pydantic model for automatic validation and API documentation"""
    gender: str
    Partner: str
    Dependents: str

    PhoneService: str
    MultipleLines: str

    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str

    Contract: str
    PaperlessBilling: str
    PaymentMethod: str

    tenure: int
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
def get_prediction(data: CustomerData):
    try:
        result = predict(data.dict())
        return {"prediction": result}
    except Exception as e:
        return {"error": str(e)}
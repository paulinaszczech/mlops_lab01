from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict

app = FastAPI()

# model jako globalna zmienna (ładowany raz przy starcie serwera)
model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request: PredictRequest):
    features = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    raw_prediction = predict(model, features)

    # Jeśli chcesz tłumaczyć na nazwy klas:
    class_names = ["setosa", "versicolor", "virginica"]
    prediction_str = class_names[int(raw_prediction)]

    return PredictResponse(prediction=prediction_str)

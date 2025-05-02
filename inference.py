import joblib


def load_model(path="model.joblib"):
    return joblib.load(path)


def predict(model, features: list[float]) -> str:
    prediction = model.predict([features])[0]
    return str(prediction)


if __name__ == "__main__":
    model = load_model()
    sample_input = [6.0, 2.9, 4.5, 1.5]  # Przykład z Iris
    result = predict(model, sample_input)
    print("Predicted class:", result)

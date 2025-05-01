import joblib


def load_model(filename="model.joblib"):
    return joblib.load(filename)


def predict(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]

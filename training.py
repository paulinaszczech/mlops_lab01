from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib


def load_data():
    return load_iris()

def train_model(data):
    model = LogisticRegression(max_iter=1000)
    model.fit(data.data, data.target)
    return model

def save_model(model, filename="model.joblib"):
    joblib.dump(model, filename)

if __name__ == "__main__":
    data = load_data()
    print("Data loaded successfully.")

    model = train_model(data)
    print("Model trained successfully.")

    save_model(model)
    print("Model saved successfully as 'model.joblib'.")

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def load_data():
    data = load_iris()
    return data.data, data.target


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    return model


def save_model(model, path="model.joblib"):
    joblib.dump(model, path)
    print(f"Model saved to {path}")


# check
if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)

import os
import joblib

# Project root directory
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Default model path
MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "saved",
    "models",
    "churn_model.pkl"
)


def save_model(model, filename=MODEL_PATH):
    """
    Save trained model using Joblib.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    joblib.dump(model, filename)
    print(f"Model saved successfully at {filename}")


def load_model(filename=MODEL_PATH):
    """
    Load trained model.
    """
    return joblib.load(filename)
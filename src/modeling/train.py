from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def train_logistic_regression(X_train, y_train):
    """
    Train a Logistic Regression model.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    model = LogisticRegression(
        random_state=42,
        max_iter=1000
    )

    model.fit(X_train_scaled, y_train)

    return model, scaler
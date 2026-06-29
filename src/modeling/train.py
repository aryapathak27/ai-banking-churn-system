from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier


def train_model(model_name, X_train, y_train):
    """
    Train a machine learning model based on the model name.
    """

    scaler = None

    if model_name == "logistic":

        scaler = StandardScaler()

        X_train = scaler.fit_transform(X_train)

        model = LogisticRegression(
            random_state=42,
            max_iter=1000
        )

    elif model_name == "decision_tree":

        model = DecisionTreeClassifier(
            random_state=42
        )

    elif model_name == "random_forest":

        model = RandomForestClassifier(
            random_state=42
        )

    elif model_name == "xgboost":

     model = XGBClassifier(
        random_state=42,
        n_estimators=200,
        max_depth=5,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss"
    )

    else:
        raise ValueError(f"Unknown model: {model_name}")

    model.fit(X_train, y_train)

    return model, scaler
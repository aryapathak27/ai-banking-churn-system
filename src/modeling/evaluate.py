from xml.parsers.expat import model

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def evaluate_model(model, scaler, X_test, y_test):
    """
    Evaluate a trained classification model.
    """
    if scaler is not None:
     X_test = scaler.transform(X_test)

    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]
    results = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "ROC AUC": roc_auc_score(y_test, y_prob),
        "Confusion Matrix": confusion_matrix(y_test, y_pred)
    }

    return results,y_pred,y_prob
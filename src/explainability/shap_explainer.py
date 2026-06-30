import shap


def create_shap_explainer(model, X_background):
    """
    Create SHAP Explainer.
    """
    return shap.Explainer(model.predict_proba, X_background)


def explain_customer(explainer, customer):
    """
    Explain a single customer.
    """
    return explainer(customer)


def plot_summary(explainer, X):
    """
    Global SHAP Summary Plot.
    """
    shap_values = explainer(X)
    shap.plots.beeswarm(shap_values[:, :, 1])


def plot_waterfall(explainer, customer):
    """
    Waterfall plot for a single customer.
    """
    shap_values = explainer(customer)

    shap.plots.waterfall(
        shap_values[0, :, 1]
    )
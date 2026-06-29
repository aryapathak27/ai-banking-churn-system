import shap


def create_shap_explainer(model):
    """
    Create SHAP TreeExplainer for XGBoost.
    """
    return shap.TreeExplainer(model)


def explain_customer(explainer, X):
    """
    Generate SHAP values.
    """
    return explainer.shap_values(X)


def plot_summary(explainer, X):
    """
    Plot SHAP summary plot.
    """
    shap_values = explainer.shap_values(X)
    shap.summary_plot(shap_values, X)


def plot_waterfall(explainer, X):
    """
    Plot SHAP waterfall plot for one customer.
    """
    shap_values = explainer(X)
    shap.plots.waterfall(shap_values[0])
"""
Feature Engineering Module
--------------------------
This module prepares features for machine learning.
"""

import pandas as pd


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature engineering on the cleaned dataset.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    # Encode Gender
    df["gender"] = df["gender"].map({
        "Female": 0,
        "Male": 1
    })

    # One-Hot Encode Geography
    df = pd.get_dummies(
        df,
        columns=["geography"],
        drop_first=True,
        dtype=int
    )

    return df
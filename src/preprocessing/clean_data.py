"""
Data Cleaning Module
--------------------
This module performs basic data cleaning before feature engineering.
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic cleaning on the customer dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Raw customer dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned dataset.
    """

    # Create a copy
    df = df.copy()

    # Remove unnecessary columns
    columns_to_drop = [
        "row_number",
        "customer_id",
        "surname"
    ]

    df.drop(columns=columns_to_drop, inplace=True)

    return df
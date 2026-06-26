"""
Database Query Module
---------------------
Contains reusable functions to fetch data from PostgreSQL.

Author: Arya Pathak
Project: AI Banking Churn Prediction System
"""

import pandas as pd

from src.database.db_connection import get_engine
from src.config import TABLE_NAME

def get_customer_data():
    """
    Retrieve the complete customer churn dataset from PostgreSQL.

    Returns:
        pandas.DataFrame
    """

    query = f"""
    SELECT *
    FROM {TABLE_NAME}
    ORDER BY row_number;
    """

    engine = get_engine()

    df = pd.read_sql(query, engine)

    return df
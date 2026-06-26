"""
Database Connection Module
--------------------------
Creates and manages the PostgreSQL database connection.

Author: Arya Pathak
Project: AI Banking Churn Prediction System
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Load the .env file from the project root
project_root = Path(__file__).resolve().parents[2]
load_dotenv(project_root / ".env")

# Read database credentials
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Validate environment variables
required_vars = {
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
}

missing = [key for key, value in required_vars.items() if not value]

if missing:
    raise ValueError(
        f"Missing environment variables in .env: {', '.join(missing)}"
    )


def get_engine():
    """
    Create and return a SQLAlchemy engine.
    """

    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(connection_string)


def test_connection():
    """
    Test whether the database connection works.
    """

    try:
        engine = get_engine()

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        print("Database connection successful!")

    except SQLAlchemyError as error:
        print(f" Database connection failed:\n{error}")
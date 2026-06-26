"""
Test Database Queries
"""

from src.database.queries import get_customer_data


def main():
    df = get_customer_data()

    print("\nFirst 5 Records\n")
    print(df.head())

    print("\nDataset Shape\n")
    print(df.shape)

    print("\nColumn Names\n")
    print(df.columns.tolist())


if __name__ == "__main__":
    main()
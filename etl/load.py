import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from pathlib import Path


PROCESSED_DATA_DIR = Path("data/processed")


DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "healthcare_db",
    "user": "merine",
    "password": " ",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def load_table(df: pd.DataFrame, table_name: str, conn):
    cols = list(df.columns)
    values = [tuple(x) for x in df.to_numpy()]

    query = f"INSERT INTO {table_name} ({','.join(cols)}) VALUES %s"

    with conn.cursor() as cursor:
        execute_values(cursor, query, values)

    conn.commit()


def load_all():
    conn = get_connection()

    admissions = pd.read_csv(PROCESSED_DATA_DIR / "admissions_processed.csv")
    bed = pd.read_csv(PROCESSED_DATA_DIR / "bed_occupancy_processed.csv")
    theatre = pd.read_csv(PROCESSED_DATA_DIR / "theatre_bookings_processed.csv")

    load_table(admissions, "admissions", conn)
    load_table(bed, "bed_occupancy", conn)
    load_table(theatre, "theatre_bookings", conn)

    conn.close()
    print("Data loaded successfully")


if __name__ == "__main__":
    load_all()

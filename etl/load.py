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


PRIMARY_KEYS = {
    "admissions": "admission_id",
    "bed_occupancy": "record_id",
    "theatre_bookings": "booking_id",
    "patient_referrals": "referral_id",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def load_table(df: pd.DataFrame, table_name: str, conn):
    cols = list(df.columns)
    values = [tuple(x) for x in df.to_numpy()]

    primary_key = PRIMARY_KEYS.get(table_name)

    if not primary_key:
        raise ValueError(f"No primary key defined for table: {table_name}")

    query = f"""
        INSERT INTO {table_name} ({','.join(cols)})
        VALUES %s
        ON CONFLICT ({primary_key}) DO NOTHING
    """

    with conn.cursor() as cursor:
        execute_values(cursor, query, values)

    conn.commit()

    print(f"Loaded {len(values)} rows into {table_name} with duplicate-safe incremental logic.")


def load_all():
    conn = get_connection()

    try:
        admissions = pd.read_csv(PROCESSED_DATA_DIR / "admissions_processed.csv")
        bed = pd.read_csv(PROCESSED_DATA_DIR / "bed_occupancy_processed.csv")
        theatre = pd.read_csv(PROCESSED_DATA_DIR / "theatre_bookings_processed.csv")
        patient_referrals = pd.read_csv(PROCESSED_DATA_DIR / "patient_referrals_processed.csv")

        load_table(admissions, "admissions", conn)
        load_table(bed, "bed_occupancy", conn)
        load_table(theatre, "theatre_bookings", conn)
        load_table(patient_referrals, "patient_referrals", conn)

        print("Data loaded successfully")

    finally:
        conn.close()


if __name__ == "__main__":
    load_all()

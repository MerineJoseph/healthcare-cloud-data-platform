import os
from pathlib import Path

import pandas as pd
import snowflake.connector
from dotenv import load_dotenv


load_dotenv()

PROCESSED_DATA_DIR = Path("data/processed")


def get_snowflake_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )


def load_dataframe_to_snowflake(df: pd.DataFrame, table_name: str, conn) -> None:
    cursor = conn.cursor()

    try:
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))

        insert_sql = f"""
            INSERT INTO {table_name} ({columns})
            VALUES ({placeholders})
        """

        records = [tuple(row) for row in df.to_numpy()]
        cursor.executemany(insert_sql, records)

        conn.commit()
        print(f"Loaded {len(records)} rows into {table_name}")

    finally:
        cursor.close()


def load_all_to_snowflake() -> None:
    conn = get_snowflake_connection()

    try:
        admissions = pd.read_csv(PROCESSED_DATA_DIR / "admissions_processed.csv")
        bed_occupancy = pd.read_csv(PROCESSED_DATA_DIR / "bed_occupancy_processed.csv")
        theatre_bookings = pd.read_csv(PROCESSED_DATA_DIR / "theatre_bookings_processed.csv")

        load_dataframe_to_snowflake(admissions, "ADMISSIONS", conn)
        load_dataframe_to_snowflake(bed_occupancy, "BED_OCCUPANCY", conn)
        load_dataframe_to_snowflake(theatre_bookings, "THEATRE_BOOKINGS", conn)

    finally:
        conn.close()


if __name__ == "__main__":
    load_all_to_snowflake()

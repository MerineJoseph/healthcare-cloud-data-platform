import pandas as pd
from pathlib import Path


RAW_DATA_DIR = Path("data/raw")


def read_csv_file(file_name: str) -> pd.DataFrame:
    file_path = RAW_DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Source file not found: {file_path}")

    df = pd.read_csv(file_path)
    return df


def extract_all_sources() -> dict:
    admissions = read_csv_file("admissions.csv")
    bed_occupancy = read_csv_file("bed_occupancy.csv")
    theatre_bookings = read_csv_file("theatre_bookings.csv")

    return {
        "admissions": admissions,
        "bed_occupancy": bed_occupancy,
        "theatre_bookings": theatre_bookings,
    }


if __name__ == "__main__":
    sources = extract_all_sources()

    for source_name, df in sources.items():
        print(f"{source_name}: {df.shape[0]} rows, {df.shape[1]} columns")

import pandas as pd
from pathlib import Path


PROCESSED_DATA_DIR = Path("data/processed")
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)


def transform_admissions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["admission_datetime"] = pd.to_datetime(df["admission_datetime"])
    df["discharge_datetime"] = pd.to_datetime(df["discharge_datetime"])

    df["length_of_stay_days"] = (
        df["discharge_datetime"] - df["admission_datetime"]
    ).dt.total_seconds() / 86400

    df["ward"] = df["ward"].str.strip().str.title()
    df["admission_type"] = df["admission_type"].str.strip().str.title()

    return df


def transform_bed_occupancy(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"]).dt.date
    df["beds_available"] = df["beds_available"].astype(int)
    df["beds_occupied"] = df["beds_occupied"].astype(int)

    df["occupancy_rate"] = (
        df["beds_occupied"] / df["beds_available"]
    ).round(4)

    df["ward"] = df["ward"].str.strip().str.title()

    return df


def transform_theatre_bookings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["surgery_date"] = pd.to_datetime(df["surgery_date"]).dt.date
    df["specialty"] = df["specialty"].str.strip().str.title()
    df["status"] = df["status"].str.strip().str.title()

    df["is_cancelled"] = df["status"].isin(["Cancelled", "Did Not Attend"])

    return df


def transform_all_sources(sources: dict) -> dict:
    transformed = {
        "admissions": transform_admissions(sources["admissions"]),
        "bed_occupancy": transform_bed_occupancy(sources["bed_occupancy"]),
        "theatre_bookings": transform_theatre_bookings(sources["theatre_bookings"]),
    }

    return transformed


def save_processed_data(transformed_sources: dict) -> None:
    for source_name, df in transformed_sources.items():
        output_path = PROCESSED_DATA_DIR / f"{source_name}_processed.csv"
        df.to_csv(output_path, index=False)
        print(f"Saved processed file: {output_path}")


if __name__ == "__main__":
    from extract import extract_all_sources

    raw_sources = extract_all_sources()
    transformed_sources = transform_all_sources(raw_sources)
    save_processed_data(transformed_sources)

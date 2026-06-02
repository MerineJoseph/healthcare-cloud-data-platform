import pandas as pd


def check_not_null(df: pd.DataFrame, columns: list[str], dataset_name: str) -> None:
    for column in columns:
        missing_count = df[column].isna().sum()

        if missing_count > 0:
            raise ValueError(
                f"{dataset_name}: Column '{column}' has {missing_count} missing values"
            )


def check_date_order(
    df: pd.DataFrame,
    start_col: str,
    end_col: str,
    dataset_name: str
) -> None:
    invalid_rows = df[df[end_col] < df[start_col]]

    if not invalid_rows.empty:
        raise ValueError(
            f"{dataset_name}: Found {len(invalid_rows)} rows where {end_col} is before {start_col}"
        )


def check_bed_capacity(df: pd.DataFrame) -> None:
    invalid_rows = df[df["beds_occupied"] > df["beds_available"]]

    if not invalid_rows.empty:
        raise ValueError(
            f"bed_occupancy: Found {len(invalid_rows)} rows where occupied beds exceed available beds"
        )


def check_non_negative(df: pd.DataFrame, columns: list[str], dataset_name: str) -> None:
    for column in columns:
        invalid_rows = df[df[column] < 0]

        if not invalid_rows.empty:
            raise ValueError(
                f"{dataset_name}: Column '{column}' has {len(invalid_rows)} negative values"
            )


def check_allowed_values(
    df: pd.DataFrame,
    column: str,
    allowed_values: list[str],
    dataset_name: str
) -> None:
    invalid_rows = df[~df[column].isin(allowed_values)]

    if not invalid_rows.empty:
        invalid_values = invalid_rows[column].unique().tolist()

        raise ValueError(
            f"{dataset_name}: Column '{column}' has invalid values: {invalid_values}"
        )


def run_data_quality_checks(transformed_sources: dict) -> None:
    admissions = transformed_sources["admissions"]
    bed_occupancy = transformed_sources["bed_occupancy"]
    theatre_bookings = transformed_sources["theatre_bookings"]

    check_not_null(
        admissions,
        ["admission_id", "patient_id", "ward", "admission_datetime"],
        "admissions"
    )

    check_date_order(
        admissions,
        "admission_datetime",
        "discharge_datetime",
        "admissions"
    )

    check_not_null(
        bed_occupancy,
        ["record_id", "date", "ward", "beds_available", "beds_occupied"],
        "bed_occupancy"
    )

    check_non_negative(
        bed_occupancy,
        ["beds_available", "beds_occupied", "occupancy_rate"],
        "bed_occupancy"
    )

    check_bed_capacity(bed_occupancy)

    check_not_null(
        theatre_bookings,
        ["booking_id", "patient_id", "surgery_date", "specialty", "status"],
        "theatre_bookings"
    )

    check_allowed_values(
        theatre_bookings,
        "status",
        ["Completed", "Cancelled", "Did Not Attend"],
        "theatre_bookings"
    )

    print("All data quality checks passed.")

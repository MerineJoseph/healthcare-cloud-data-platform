import pandas as pd
import pytest

from etl.dq_checks import check_not_null, check_date_order, check_bed_capacity


def test_check_not_null_passes_for_valid_data():
    df = pd.DataFrame({
        "admission_id": ["A001", "A002"],
        "patient_id": ["P001", "P002"]
    })

    check_not_null(df, ["admission_id", "patient_id"], "admissions")


def test_check_not_null_fails_for_missing_data():
    df = pd.DataFrame({
        "admission_id": ["A001", None],
        "patient_id": ["P001", "P002"]
    })

    with pytest.raises(ValueError):
        check_not_null(df, ["admission_id"], "admissions")


def test_check_date_order_passes_for_valid_dates():
    df = pd.DataFrame({
        "admission_datetime": pd.to_datetime(["2026-01-01"]),
        "discharge_datetime": pd.to_datetime(["2026-01-03"])
    })

    check_date_order(
        df,
        "admission_datetime",
        "discharge_datetime",
        "admissions"
    )


def test_check_date_order_fails_for_invalid_dates():
    df = pd.DataFrame({
        "admission_datetime": pd.to_datetime(["2026-01-05"]),
        "discharge_datetime": pd.to_datetime(["2026-01-03"])
    })

    with pytest.raises(ValueError):
        check_date_order(
            df,
            "admission_datetime",
            "discharge_datetime",
            "admissions"
        )


def test_check_bed_capacity_passes_for_valid_data():
    df = pd.DataFrame({
        "beds_available": [40],
        "beds_occupied": [35]
    })

    check_bed_capacity(df)


def test_check_bed_capacity_fails_when_occupied_exceeds_available():
    df = pd.DataFrame({
        "beds_available": [40],
        "beds_occupied": [45]
    })

    with pytest.raises(ValueError):
        check_bed_capacity(df)

from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")
PROFILE_OUTPUT_DIR = Path("docs/data_profiles")


def profile_dataframe(df, dataset_name):
    report = []

    report.append(f"# Data Profile Report: {dataset_name}")
    report.append("")

    report.append("## Dataset Overview")
    report.append(f"Rows: {len(df)}")
    report.append(f"Columns: {len(df.columns)}")
    report.append("")

    report.append("## Column List")

    for column in df.columns:
        report.append(f"- {column}")

    report.append("")
    report.append("## Missing Values")

    missing_values = df.isnull().sum()

    for column, count in missing_values.items():
        report.append(f"- {column}: {count}")

    report.append("")
    report.append("## Duplicate Records")

    duplicate_count = df.duplicated().sum()

    report.append(f"Duplicate Rows: {duplicate_count}")

    report.append("")
    report.append("## Column Summary")

    for column in df.columns:

        report.append("")
        report.append(f"### {column}")
        report.append(f"Data Type: {df[column].dtype}")
        report.append(f"Unique Values: {df[column].nunique()}")

        if pd.api.types.is_numeric_dtype(df[column]):

            report.append(f"Minimum: {df[column].min()}")
            report.append(f"Maximum: {df[column].max()}")
            report.append(f"Average: {round(df[column].mean(), 2)}")

    return "\n".join(report)


def generate_profiles():

    PROFILE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    datasets = {
        "admissions": RAW_DATA_DIR / "admissions.csv",
        "bed_occupancy": RAW_DATA_DIR / "bed_occupancy.csv",
        "theatre_bookings": RAW_DATA_DIR / "theatre_bookings.csv"
    }

    for dataset_name, file_path in datasets.items():

        df = pd.read_csv(file_path)

        report = profile_dataframe(df, dataset_name)

        output_file = PROFILE_OUTPUT_DIR / f"{dataset_name}_profile.md"

        with open(output_file, "w") as f:
            f.write(report)

        print(f"Created profile: {output_file}")


if __name__ == "__main__":
    generate_profiles()

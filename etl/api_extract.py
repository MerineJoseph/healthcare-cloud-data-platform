import json
import logging
from pathlib import Path

import pandas as pd


API_DATA_FILE = Path("data/api/patient_referrals_api_response.json")
RAW_DATA_DIR = Path("data/raw")
OUTPUT_FILE = RAW_DATA_DIR / "patient_referrals.csv"

logging.basicConfig(
    filename="logs/healthcare_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def extract_patient_referrals_api() -> pd.DataFrame:
    """
    Simulates REST API ingestion from a healthcare referral source.

    In production, this would be replaced with:
    - requests.get()
    - API authentication
    - pagination
    - retries
    - rate-limit handling
    - API response validation
    """

    try:
        with open(API_DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)

        df = pd.DataFrame(records)

        required_columns = [
            "referral_id",
            "patient_id",
            "referral_source",
            "referral_date",
            "priority",
            "status",
        ]

        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Missing required API fields: {missing_columns}")

        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
        df.to_csv(OUTPUT_FILE, index=False)

        logging.info("REST API data extracted successfully to %s", OUTPUT_FILE)
        print(f"REST API data extracted successfully: {OUTPUT_FILE}")

        return df

    except FileNotFoundError:
        logging.error("API mock response file not found: %s", API_DATA_FILE)
        raise

    except json.JSONDecodeError:
        logging.error("Invalid JSON format in API response file")
        raise

    except Exception as error:
        logging.error("REST API extraction failed: %s", error)
        raise


if __name__ == "__main__":
    extract_patient_referrals_api()

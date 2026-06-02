import logging
import sys
from pathlib import Path

from extract import extract_all_sources
from transform import transform_all_sources, save_processed_data
from dq_checks import run_data_quality_checks
from load import load_all


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from config.settings import LOG_FILE


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def run_pipeline():
    logging.info("Healthcare ETL pipeline started.")

    try:
        raw_sources = extract_all_sources()
        logging.info("Extraction completed successfully.")

        transformed_sources = transform_all_sources(raw_sources)
        logging.info("Transformation completed successfully.")

        run_data_quality_checks(transformed_sources)
        logging.info("Data quality checks passed.")

        save_processed_data(transformed_sources)
        logging.info("Processed files saved successfully.")

        load_all()
        logging.info("Data loaded successfully.")

        logging.info("Healthcare ETL pipeline completed successfully.")

    except Exception as error:
        logging.exception(f"Healthcare ETL pipeline failed: {error}")
        raise


if __name__ == "__main__":
    run_pipeline()

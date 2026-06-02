from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "healthcare_pipeline.log"

LOG_DIR.mkdir(parents=True, exist_ok=True)

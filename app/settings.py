import os
from uploaders import Uploader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

METRICS_FOLDER: str = os.environ.get(
    "METRICS_FOLDER", os.path.join(BASE_DIR, "metrics")
)
METRICS_PROCESSED_FOLDER: str = os.environ.get(
    "METRICS_FOLDER", os.path.join(BASE_DIR, "metrics_processed")
)
DEFAULT_UPLOADER: str = os.environ.get("DEFAULT_UPLOADER", Uploader.GOOGLE_DRIVE.value)

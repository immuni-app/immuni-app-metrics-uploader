import os
import pytest
import shutil

from app.core.models import Metrics, MetricsException


DATA_FOLDER: str = os.path.join(".", "tests")
METRICS_SAMPLE_FOLDER: str = os.path.join(DATA_FOLDER, "metrics_sample")
METRICS_DEST_FOLDER: str = os.path.join(DATA_FOLDER, "metrics")
METRICS_PROCESSED_FOLDER: str = os.path.join(DATA_FOLDER, "metrics_processed")

shutil.rmtree(METRICS_DEST_FOLDER)
shutil.rmtree(METRICS_PROCESSED_FOLDER)
os.mkdir(METRICS_PROCESSED_FOLDER)

shutil.copytree(METRICS_SAMPLE_FOLDER, METRICS_DEST_FOLDER)


def test_metrics():
    csv_file: str = os.path.join(METRICS_DEST_FOLDER, "android.csv")
    Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

    csv_file: str = os.path.join(METRICS_DEST_FOLDER, "ios.csv")
    Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

    with pytest.raises(MetricsException):
        csv_file: str = os.path.join(METRICS_DEST_FOLDER, "notexistent")
        Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

    with pytest.raises(MetricsException):
        csv_file: str = os.path.join(METRICS_DEST_FOLDER, "empty.csv")
        Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

    with pytest.raises(MetricsException):
        csv_file: str = os.path.join(METRICS_DEST_FOLDER, "invalid.csv")
        Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

    with pytest.raises(MetricsException):
        csv_file: str = os.path.join(METRICS_DEST_FOLDER, "not_valid_android.csv")
        Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

    with pytest.raises(MetricsException):
        csv_file: str = os.path.join(METRICS_DEST_FOLDER, "not_valid.ios.csv")
        Metrics(csv_file).export(os.path.join(METRICS_PROCESSED_FOLDER))

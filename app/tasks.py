import os

from core.models import Metrics, MetricsException
from settings import METRICS_FOLDER, METRICS_PROCESSED_FOLDER, DEFAULT_UPLOADER
from uploaders import get_uploader, UploaderException, UploaderObject

if not os.path.exists(METRICS_FOLDER):
    os.makedirs(METRICS_FOLDER)

if not os.path.exists(METRICS_PROCESSED_FOLDER):
    os.makedirs(METRICS_PROCESSED_FOLDER)


def process_metrics() -> None:
    for f in os.listdir(METRICS_FOLDER):
        file_path: str = os.path.join(METRICS_FOLDER, f)
        if os.path.isfile(file_path):
            try:
                metrics: Metrics = Metrics(file_path)
                metrics.export(METRICS_PROCESSED_FOLDER)
            except MetricsException as ex:
                print(ex)


def upload_metrics() -> None:
    uploader: UploaderObject = get_uploader(DEFAULT_UPLOADER)
    uploader.connect()
    for f in os.listdir(METRICS_PROCESSED_FOLDER):
        file_path: str = os.path.join(METRICS_PROCESSED_FOLDER, f)
        if os.path.isfile(file_path):
            try:
                uploader.upload(f, file_path)
            except UploaderException as ex:
                print(ex)


process_metrics()
upload_metrics()
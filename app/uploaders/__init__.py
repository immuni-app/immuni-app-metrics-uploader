from enum import Enum
from .googledrive import GoogleDriveUploader
from .uploader import UploaderObject


class UploaderException(Exception):
    pass


class Uploader(Enum):
    GOOGLE_DRIVE = "GOOGLE_DRIVE"


def get_uploader(uploader: str) -> UploaderObject:
    if uploader == Uploader.GOOGLE_DRIVE.value:
        return GoogleDriveUploader()
    raise UploaderException("Uploader not found!")

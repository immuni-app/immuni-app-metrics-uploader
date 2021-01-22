import os

from pydrive.auth import GoogleAuth  # type: ignore
from pydrive.drive import GoogleDrive  # type: ignore

from .uploader import UploaderObject


class GoogleDriveUploader(UploaderObject):
    def connect(self):
        gauth: GoogleAuth = GoogleAuth()
        self._drive: GoogleDrive = GoogleDrive(gauth)

    def upload(self, name: str, file_path: str):
        parent_folder_id: str = os.environ.get("GDRIVE_PARENT_FOLDER_ID", "")
        parents: list = []
        if parent_folder_id:
            parents.append({"id": parent_folder_id})
        f = self._drive.CreateFile({"title": name, "parents": parents})
        f.SetContentFile(file_path)
        f.Upload()

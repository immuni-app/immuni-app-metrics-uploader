import csv
import locale
import os
import shutil

from datetime import datetime
from enum import Enum


locale.setlocale(locale.LC_TIME, "")


class Platform(Enum):
    IOS = "IOS"
    ANDROID = "ANDROID"


class MetricsException(Exception):
    pass


class Metrics:
    def __init__(self, csv_file_path: str):
        self._csv_file_path: str = csv_file_path
        try:
            self._parse_csv_file()
        except UnicodeDecodeError:
            raise MetricsException("Unable to read the file")
        except FileNotFoundError:
            raise MetricsException("Unable to find the file")

    def _parse_csv_file(self) -> None:
        with open(self._csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count: int = 0
            row: list = []
            for row in csv_reader:
                if line_count == 0:
                    self._platform: Platform = self._detect_platform(row[0])
                line_count += 1
            if not row:
                raise MetricsException("File is empty")
            self._report_date: str = self._format_date(row[0])

    def _detect_platform(self, cell: str) -> Platform:
        if cell == "Nome":
            return Platform.IOS
        elif cell == "Data":
            return Platform.ANDROID
        raise MetricsException("Platform does not exist")

    def _format_date(self, date: str) -> str:
        date_time_obj: datetime
        try:
            if self.platform == Platform.IOS:
                date_time_obj = datetime.strptime(date, "%d/%m/%y")
            elif self.platform == Platform.ANDROID:
                date_time_obj = datetime.strptime(date, "%d %b %Y")
            return date_time_obj.strftime("%d%m%Y")
        except ValueError:
            raise MetricsException("Error formatting date")

    @property
    def platform(self) -> Platform:
        return self._platform

    @property
    def report_date(self) -> str:
        return self._report_date

    def export(self, destination) -> None:
        exported_filename: str = f"IMMUNI_{self.platform.value}_{self.report_date}.csv"
        shutil.move(self._csv_file_path, os.path.join(destination, exported_filename))

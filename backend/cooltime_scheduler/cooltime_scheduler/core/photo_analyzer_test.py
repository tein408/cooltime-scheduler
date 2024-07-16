"""Photo Analyzer unittest"""

from photo_analyzer import PhotoAnalyzer
import pytest
import tempfile
import os
from pathlib import Path


def test_calculate_calories():
    photo_name = "image_dump"
    analyzer = PhotoAnalyzer()
    temp_dir = tempfile.mkdtemp()
    original_bytes = Path(os.getcwd()).joinpath("backend/cooltime_scheduler/cooltime_scheduler/resources/image1.jpg").read_bytes()
    Path(temp_dir).joinpath(photo_name).write_bytes(original_bytes)

    bytes = analyzer.calculate_calories(os.path.join(temp_dir, photo_name))

    assert original_bytes == bytes

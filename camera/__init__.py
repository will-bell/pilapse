# Export these through the `camera` module
from camera.cameraimpl import Camera
from camera.CameraHandler import CameraHandler
from typing import Optional

CameraConfig = dict[str, Optional[str]]
CaptureMetadata = dict[str, Optional[str]]

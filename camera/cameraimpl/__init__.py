import os
from typing import Any, Tuple
if os.getenv('CAMERA_PLATFORM') == 'PILAPSE':
  from picamera2 import Picamera2 # type: ignore
  
  # Camera = Picamera2
  
  def new_camera(size: Tuple[int, int] = (1600, 1200)) -> Any:
    camera = Picamera2()
    camera.still_configuration.size = size
    camera.still_configuration.enable_raw()
    camera.still_configuration.raw.size = camera.sensor_resolution
    
    return camera
  
else:
  from .FakeCamera import MockCamera
  
  def new_camera(size: Tuple[int, int] = (1600, 1200)) -> Any:
    return MockCamera()

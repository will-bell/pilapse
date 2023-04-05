import os
if os.getenv('CAMERA_PLATFORM') == 'PILAPSE':
  from picamera2 import Picamera # type: ignore
  Camera = Picamera
  
else:
  from .FakeCamera import Camera

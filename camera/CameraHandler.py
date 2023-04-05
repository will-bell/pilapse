import time
from typing import Optional
from camera import Camera

class CameraHandler(object):
  _cameraimpl: Optional[Camera]

  def __init__(self):
    self._cameraimpl = None
    
  def __enter__(self):
    self._cameraimpl = Camera()
    self._cameraimpl.start()
    time.sleep(2)
    return self._cameraimpl
  
  def __exit__(self, *args):
    if self._cameraimpl:
      self._cameraimpl.close()
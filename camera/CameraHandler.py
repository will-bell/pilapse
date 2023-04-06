from typing import Any, Tuple
import time
from typing import Optional
from camera import new_camera

class CameraHandler(object):
  _cameraimpl: Optional[Any]
  _size: Tuple[int, int]
  
  def __init__(self, size: Tuple[int, int] = (1600, 1200)):
    self._cameraimpl = None
    self._size = size
    
  def __enter__(self):
    self._cameraimpl = new_camera(self._size)
    
    self._cameraimpl.start("still")
    time.sleep(2)
    return self._cameraimpl
  
  def __exit__(self, *args):
    if self._cameraimpl:
      self._cameraimpl.close()

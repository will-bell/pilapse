from typing import Callable

class CameraHandler:
  _cameraConstructor: Callable[[], float]
  
  def __init__(self, cameraConstructor: Callable):
    pass
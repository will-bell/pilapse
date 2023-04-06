from logging import Logger
import time
from typing import Callable, Optional

EventFuncType = Callable[[Optional[Logger]], None]

class Timer:
  _func: Callable[[Optional[Logger]], None]
  _last_time: float
  _wait_interval: float
  _logger: Optional[Logger]
  
  def __init__(self, func: EventFuncType, wait_interval: float, logger: Optional[Logger]):
    self._func = func
    self._last_time = time.time() - wait_interval # to start us off
    self._wait_interval = wait_interval
    self._logger = logger
  
  def check(self):
    if time.time() - self._last_time > self._wait_interval:
      self._func(self._logger)
      self._last_time = time.time()

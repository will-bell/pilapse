from concurrent.futures import thread
from logging import Logger
import sched
import time
from scheduler.Timer import EventFuncType, Timer
from typing import Callable, Optional, Tuple
import threading

def timerLoop(timer: Timer, check_interval: float = 1):
  while True:
    timer.check()
    time.sleep(check_interval)

class Scheduler:
  _timers: list[Timer]
  _threads: list[threading.Thread]
  
  def __init__(self, events: list[Tuple[EventFuncType, float]], logger: Optional[Logger] = None):
    self._timers = [Timer(func, wait_interval, logger) for func, wait_interval in events]
    self._threads = []
    
  def run(self):
    # make the threads
    for timer in self._timers:
      self._threads.append(threading.Thread(target=timerLoop, args=(timer,), daemon=True))
    
    # start the threads
    for thread in self._threads:
      thread.start()

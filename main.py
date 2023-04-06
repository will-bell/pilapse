from logging import Logger
import logging
import time
from camera import CameraHandler
from dotenv import load_dotenv
from typing import Optional
import numpy as np

from scheduler import Scheduler

from flask import Flask, render_template, send_from_directory, url_for
import os

IMAGES_DIR = os.path.relpath("images")

app = Flask(__name__)

@app.route('/latest_image')
def latest_image():
  images = os.listdir(IMAGES_DIR)
  
  latestind = 0
  maxctime = -1
  for ind, image in enumerate(images):
    ctime = os.path.getctime(os.path.join(IMAGES_DIR, image))
    if ctime > maxctime:
      latestind = ind
      maxctime = ctime
    
  return send_from_directory('images', images[latestind])

@app.route('/')
def index():
  return render_template('index.html', latest_image=url_for('latest_image'))

def take_a_picture(logger: Optional[Logger] = None):
  with CameraHandler() as camera:
    camera.capture_file(f'images/noise_at_{time.time()}.jpg')
    
  if logger:
    logger.info("Took a picture")

if __name__ == '__main__':
  load_dotenv('.env')
  logger = logging.getLogger(__name__)
  
  Scheduler([(take_a_picture, 2)], logger).run()
  
  app.run(host='0.0.0.0', debug=False)

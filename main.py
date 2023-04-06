from logging import Logger
import logging
import time
from camera import CameraHandler
from dotenv import load_dotenv
from typing import Optional

from scheduler import Scheduler

from flask import Flask, render_template, send_from_directory, url_for
import os

IMAGES_DIR = os.path.relpath("images")

app = Flask(__name__)

@app.route('/latest_image')
def latest_image():
  latest_image = os.listdir(IMAGES_DIR)[-1]
  return send_from_directory('images', latest_image)

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
  
  Scheduler([(take_a_picture, 10)], logger).run()
  
  app.run(debug=False)
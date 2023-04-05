from camera import CameraHandler
from dotenv import load_dotenv

if __name__ == '__main__':
  load_dotenv('.env')
  with CameraHandler() as camera:
    camera.capture_file('images/test.jpg')
import numpy as np
from PIL import Image

def random100by100(file_output: str) -> None:
  imarray = np.random.rand(1000, 1000, 3) * 255
  im = Image.fromarray(imarray.astype('uint8')).convert('RGB')
  im.save(file_output)

class Camera:
    def start(self) -> None:
      print("'Starting' camera")
    
    def close(self) -> None:
      print("'Closing' camera")
      
    def capture_file(self, file_output: str, name: str = "main"):
      print(f"'Capturing' image and writing to {file_output}")
      random100by100(file_output)
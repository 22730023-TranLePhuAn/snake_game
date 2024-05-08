
import random
from config import Config

# tạo đối tượng Quả táo (thức ăn) trong trò chơi
class Apple():
  def __init__(self):
    self.setNewLocation()
  # đặt vị trí mới cho Quả táo
  def setNewLocation(self):
    self.x = random.randint(0, Config.CELLWIDTH - 1)
    self.y = random.randint(0, Config.CELLHEIGHT - 1)

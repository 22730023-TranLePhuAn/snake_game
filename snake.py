from config import Config
import random

# tạo con rắn và xử lý di chuyển
class Snake():
  # khai báo để đại diện cho các hướng di chuyển và đầu của con rắn
  UP = 'up'
  DOWN = 'down'
  LEFT = 'left'
  RIGHT = 'right'
  HEAD = 0

  # con rắn được khởi tạo với một vị trí ngẫu nhiên và một hướng di chuyển khởi đầu.
  # mảng wormCoords chứa các tọa độ của các phần thân của con rắn, bắt đầu với đầu rắn và hai phần thân liền kề.
  def __init__(self):
    self.x = random.randint(5, Config.CELLWIDTH - 6)
    self.y = random.randint(5, Config.CELLHEIGHT - 6)
    self.direction = self.RIGHT
    self.wormCoords = [
        {'x': self.x, 'y': self.y},
        {'x': self.x - 1, 'y': self.y},
        {'x': self.x - 2, 'y': self.y}
    ]

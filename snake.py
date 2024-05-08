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

  #cập nhật vị trí của con rắn và kiểm tra xem con rắn có ăn quả táo không
  def update(self, apple):
    # Nếu đầu con rắn trùng vị trí với quả táo (apple), quả táo được đặt lại ở vị trí mới. 
    if self.wormCoords[self.HEAD]['x'] == apple.x and self.wormCoords[self.HEAD]['y'] == apple.y:
      apple.setNewLocation()
    else:
      del self.wormCoords[-1]  # Ngược lại, phần thân cuối cùng của con rắn được loại bỏ để tạo hiệu ứng di chuyển.
      
    # vị trí mới của đầu con rắn được tạo thành từ tọa độ x và y của đầu con rắn hiện tại và được thêm vào phần đầu của mảng wormCoords.
    if self.direction == self.UP:
      newHead = {'x': self.wormCoords[self.HEAD]['x'],
                 'y': self.wormCoords[self.HEAD]['y'] - 1}
    elif self.direction == self.DOWN:
      newHead = {'x': self.wormCoords[self.HEAD]['x'],
                 'y': self.wormCoords[self.HEAD]['y'] + 1}
    elif self.direction == self.LEFT:
      newHead = {'x': self.wormCoords[self.HEAD]['x'] - 1,
                 'y': self.wormCoords[self.HEAD]['y']}
    elif self.direction == self.RIGHT:
      newHead = {'x': self.wormCoords[self.HEAD]['x'] + 1,
                 'y': self.wormCoords[self.HEAD]['y']}
    self.wormCoords.insert(0, newHead)
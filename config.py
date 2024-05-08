
# tạo cấu hình cho trò chơi, bao gồm kích thước cửa sổ, kích thước ô vuông, màu sắc và tốc độ khung hình.
class Config():
  FPS = 9                       # Số khung hình trên giây được sử dụng trong trò chơi.
  MENU_FPS = 60                 # Số khung hình trên giây được sử dụng trong menu.
  WINDOW_WIDTH = 640            # Chiều rộng của cửa sổ trò chơi.
  WINDOW_HEIGHT = 480           # Chiều cao của cửa sổ trò chơi.
  CELLSIZE = 20                 # Kích thước của mỗi ô vuông trong lưới.
  assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
  assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
  CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)      # Số ô vuông theo chiều ngang của lưới.
  CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE)    # Số ô vuông theo chiều dọc của lưới.

  # Colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  DARKRED = (139, 0, 0)
  DARKGREEN = (0, 155, 0)
  DARKGRAY = (40, 40, 40)
  BG_COLOR = BLACK         # Màu nền của cửa sổ trò chơi.

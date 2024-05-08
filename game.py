from config import Config
from snake import Snake
from apple import Apple
import pygame
import sys


class Game():
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode(
        (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    self.clock = pygame.time.Clock()
    self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')
    self.apple = Apple()
    self.snake = Snake()

  # Vẽ lưới trên màn hình pygame
  def drawGrid(self):
    # vẽ đường dọc
    for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY,
                       (x, 0), (x, Config.WINDOW_HEIGHT))
    # vẽ đường ngang
    for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY,
                       (0, y), (Config.WINDOW_WIDTH, y))

  # Vẽ con rắn lên màn hình pygame.
  def drawWorm(self):
    for coord in self.snake.wormCoords:
      x = coord['x'] * Config.CELLSIZE
      y = coord['y'] * Config.CELLSIZE
      wormSegmentReact = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
      pygame.draw.rect(self.screen, Config.DARKGREEN, wormSegmentReact)
      wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8)
      pygame.draw.rect(self.screen, Config.GREEN, wormInnerSegmentRect)

  # Vẽ quả táo lên màn hình pygame.
  def drawApple(self):
    x = self.apple.x * Config.CELLSIZE
    y = self.apple.y * Config.CELLSIZE
    appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
    pygame.draw.rect(self.screen, Config.DARKRED, appleRect)
    appleInnerRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8)
    pygame.draw.rect(self.screen, Config.RED, appleInnerRect)

  # Vẽ điểm số lên màn hình pygame.
  def drawScore(self, score):
    scoreSurf = self.BASICFONT.render('Score: %s' % (score), True, Config.WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Config.WINDOW_WIDTH - 120, 10)
    self.screen.blit(scoreSurf, scoreRect)

  # Vẽ các phần tử của trò chơi (lưới, con rắn, quả táo, điểm số) lên màn hình pygame.
  def draw(self):
    self.screen.fill(Config.BG_COLOR)
    
    self.drawGrid()
    self.drawWorm()
    self.drawApple()
    self.drawScore(len(self.snake.wormCoords) - 3)
    pygame.display.update()
    self.clock.tick(Config.FPS)

  # Kiểm tra xem người dùng có nhấn phím nào không và xử lý khi người dùng nhấn phím ESC để thoát.
  def checkForKeyPress(self):
    if len(pygame.event.get(pygame.QUIT)) > 0:
      pygame.quit()

    keyUpEvents = pygame.event.get(pygame.KEYUP)

    if len(keyUpEvents) == 0:
      return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
      pygame.quit()
      quit()
    return keyUpEvents[0].key

  # Xử lý các sự kiện phím được nhận từ người dùng. Hàm này xác định hướng di chuyển mới của con rắn dựa trên các phím di chuyển được nhấn.
  def handleKeyEvents(self, event):
    if(event.key == pygame.K_LEFT or event.key == pygame.K_a) and (self.snake.direction != self.snake.RIGHT):
      self.snake.direction = self.snake.LEFT
    elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (self.snake.direction != self.snake.LEFT):
      self.snake.direction = self.snake.RIGHT
    elif(event.key == pygame.K_UP or event.key == pygame.K_w) and (self.snake.direction != self.snake.DOWN):
      self.snake.direction = self.snake.UP
    elif(event.key == pygame.K_DOWN or event.key == pygame.K_s) and (self.snake.direction != self.snake.UP):
      self.snake.direction = self.snake.DOWN
    elif event.key == pygame.K_ESCAPE:
      pygame.quit()

  # Đặt lại trạng thái của trò chơi. Hàm này xóa con rắn và quả táo hiện tại và tạo mới chúng để bắt đầu một ván mới.
  def resetGame(self):
    del self.snake
    del self.apple
    self.snake = Snake()
    self.apple = Apple()

    return True

  # Vẽ thông báo yêu cầu người chơi nhấn một phím để chơi lại.
  def drawPressKeyMgs(self):
    pressKeySurf = self.BASICFONT.render('Press a key UP to play again', True, Config.WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (Config.WINDOW_WIDTH - 250, Config.WINDOW_HEIGHT - 30)
    self.screen.blit(pressKeySurf, pressKeyRect)

  # Xử lý va chạm của con rắn với tường hoặc chính nó. Nếu va chạm sẽ gọi resetGame() để chuẩn bị một ván mới.
  def isGameOver(self):
    if(self.snake.wormCoords[self.snake.HEAD]['x'] == -1 or
            self.snake.wormCoords[self.snake.HEAD]['x'] == Config.CELLWIDTH or
            self.snake.wormCoords[self.snake.HEAD]['y'] == -1 or
            self.snake.wormCoords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
      return self.resetGame()
    for wormBody in self.snake.wormCoords[1:]:
      if wormBody['x'] == self.snake.wormCoords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCoords[self.snake.HEAD]['y']:
        return self.resetGame()

  # Hiển thị màn hình khởi đầu của trò chơi. Hàm này hiển thị tiêu đề "Snake!" và quay các chữ theo góc để tạo hiệu ứng.
  def showStartScreen(self):
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake!', True, Config.WHITE, Config.DARKGREEN)
    titleSurf2 = titleFont.render('Snake!', True, Config.GREEN)
    degrees1 = 0
    degrees2 = 0
    while True:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          return
      self.screen.fill(Config.BG_COLOR)

      rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
      rotatedRect1 = rotatedSurf1.get_rect()
      rotatedRect1.center = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
      self.screen.blit(rotatedSurf1, rotatedRect1)

      rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
      rotatedRect2 = rotatedSurf2.get_rect()
      rotatedRect2.center = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
      self.screen.blit(rotatedSurf2, rotatedRect2)

      self.drawPressKeyMgs()

      pygame.display.update()
      self.clock.tick(Config.MENU_FPS)
      degrees1 += 1  # rotate by 3degrees each frame
      degrees2 += 2  # rotate by 7degrees each frame

  # Hiển thị tiêu đề "Game Over" và thông báo yêu cầu người chơi nhấn một phím để chơi lại.
  

  # Chạy trò chơi. Hàm này gọi showStartScreen() và sau đó lặp đi lặp lại gameLoop() cho đến khi trò chơi kết thúc.
  def run(self):
    self.showStartScreen()

    while True:
      self.gameLoop()
      self.displayGameOver()

  # Vòng lặp chính của trò chơi, lắng nghe các sự kiện từ bàn phím, cập nhật trạng thái của con rắn, gọi các hàm vẽ và kiểm tra xem trò chơi đã kết thúc chưa.
  def gameLoop(self):
    while True:  # main game loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          self.handleKeyEvents(event)

      self.snake.update(self.apple)
      self.draw()
      if self.isGameOver():
        break

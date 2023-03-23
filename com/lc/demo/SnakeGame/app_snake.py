import pygame
import random
import sys

# by chatGPT
# BAI Chat
# https://chatbot.theb.ai/#/chat

# 初始化pygame
pygame.init()

# 定义常量
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRID_SIZE = 20

# 创建屏幕对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('贪吃蛇')

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 定义字体
font = pygame.font.SysFont(None, 30)


# 定义蛇类
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0] * GRID_SIZE,
                self.body[0][1] + self.direction[1] * GRID_SIZE)
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        tail = (self.body[-1][0], self.body[-1][1])
        self.body.append(tail)

    def collide_with_wall(self):
        if (self.body[0][0] < 0 or self.body[0][0] >= SCREEN_WIDTH or
                self.body[0][1] < 0 or self.body[0][1] >= SCREEN_HEIGHT):
            return True
        return False

    def collide_with_self(self):
        for i in range(1, len(self.body)):
            if self.body[i] == self.body[0]:
                return True
        return False


# 定义食物类
class Food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
        self.y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE

    def draw(self):
        rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)


# 初始化蛇和食物
snake = Snake()
food = Food()

# 游戏循环
clock = pygame.time.Clock()
score = 0
while True:
    clock.tick(10)

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    # 移动蛇
    snake.move()

    # 判断是否撞墙或者自己
    if snake.collide_with_wall() or snake.collide_with_self():
        print('game over')
        pygame.quit()
        sys.exit()

    # 判断是否吃到食物
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        snake.grow()
        score += 10
        food = Food()

    # 绘制背景
    screen.fill(WHITE)

    # 绘制蛇
    for x, y in snake.body:
        rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, BLACK, rect)

    # 绘制食物
    food.draw()

    # 绘制分数
    score_text = font.render('Score: %d' % score, True, BLACK)
    screen.blit(score_text, (10, 10))

    # 更新屏幕
    pygame.display.update()

    # 输出两次
    print("Score: %d" % score)
    print("Snake Length: %d" % len(snake.body))

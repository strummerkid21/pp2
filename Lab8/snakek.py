import pygame
from color_palette import *
import random
pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((HEIGHT, WIDTH))
font=pygame.font.Font(None,36)
CELL = 30
#фон
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)
#шах порядок
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
#змейка
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow=False
#движение
    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        
        # wall collision
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return False  
        # self collision
        if new_head in self.body:
            return False  
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True
    def check_collision_wall(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_collision_self(self):
        return self.body[0] in self.body[1:]

        
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
      if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
        self.grow = True 
        return True  
      return False


 
class Food:
    def __init__(self, snake):
        self.spawn(snake)
    def spawn(self, snake):
      while True:
        new_pos = Point(random.randint(0, (WIDTH // CELL) - 1), random.randint(0, (HEIGHT // CELL) - 1))
        if new_pos not in snake.body:  
            self.pos = new_pos
            break


    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


#переменные
FPS = 5
clock = pygame.time.Clock()
snake = Snake()
food = Food(snake)
score=0
level=1

running = True
while running:
    screen.fill(colorBLACK)
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()
    if not snake.move() or snake.check_collision_wall() or snake.check_collision_self():
        print("Game Over!")
        break

    if snake.check_collision(food):
        score += 1  
        if score % 3 == 0:  # уровень за каждые 3 
            level += 1
            FPS += 1  # скорость
        food.spawn(snake)  # новая еда


 
  
    snake.draw()
    food.draw()
    score_text = font.render(f"Score: {score}", True, colorBLACK)
    level_text = font.render(f"Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
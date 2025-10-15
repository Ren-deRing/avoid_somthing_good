from scene import Scene
from scenes.menu import MainMenu
import colors
import dotenv
import pygame
import os

dotenv.load_dotenv()

# Constants
FPS = int(os.getenv("FPS", "60"))
WIDTH = int(os.getenv("WIDTH", "600"))
HEIGHT = int(os.getenv("HEIGHT", "600"))

# Init
is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

current_stage: Scene = MainMenu(screen)
pygame.init()

# 게임 루프
while is_running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        current_stage.handle_event(event)
    
    screen.fill(colors.BLACK)

    current_stage._update(dt)
    current_stage._draw()

    pygame.display.update()

pygame.quit()
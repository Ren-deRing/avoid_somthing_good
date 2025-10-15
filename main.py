from stage import Stage
from stages.menu import MainMenu
import dotenv
import pygame
import os

dotenv.load_dotenv()

# Constants
FPS = int(os.getenv("FPS"))
WIDTH = int(os.getenv("WIDTH"))
HEIGHT = int(os.getenv("HEIGHT"))

# Init
is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

current_stage: Stage = MainMenu(screen)
pygame.init()

# 게임 루프
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        current_stage._on_event(event)
    
    current_stage.update()
    current_stage.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
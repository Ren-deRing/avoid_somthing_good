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
pygame.init()

is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

current_scene: Scene = MainMenu(screen)

# 게임 루프
while is_running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        current_scene.handle_event(event)
    
    screen.fill(colors.BLACK)

    current_scene._update(dt)
    current_scene._draw()

    pygame.display.update()

pygame.quit()
from scene import Scene
from scenes.menu import MainMenu
from manager import SceneManager
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

# Scene Manager
scenes: list[Scene] = [MainMenu(screen)]
scene_manager: SceneManager = SceneManager(scenes)

# 게임 루프
while is_running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        scene_manager._on_event(event)
    
    screen.fill(colors.BLACK)

    scene_manager._update(dt)
    scene_manager._draw()

    pygame.display.update()

pygame.quit()
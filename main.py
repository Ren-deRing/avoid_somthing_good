from scene import Scene
from scenes import avoid, menu
from manager import SceneManager
from typing import Type
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
scenes: list[Type[Scene]] = [avoid.AvoidScene, menu.MainMenuScene]
scene_manager: SceneManager = SceneManager(screen, scenes)

# 초기 Scene 설정
scene_manager.add_scene_to_render('AvoidScene')

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
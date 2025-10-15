import pygame
from object import GameObject

class Scene:
    def __init__(self, screen: pygame.Surface, objects: list[GameObject]):
        self.screen = screen
        self.objects = objects

    def update(self, dt: float):
        pass

    def handle_event(self, event: pygame.event.Event):
        pass

    def _update(self, dt: float):
        self.update(dt)
        for obj in self.objects:
            obj._update(dt)

    def _draw(self):
        for obj in self.objects:
            obj._draw(self.screen)
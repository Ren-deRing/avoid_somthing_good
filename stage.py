import pygame
from object import GameObject

class Stage:
    def __init__(self, screen: pygame.Surface, objects: list[GameObject]):
        self.screen = screen
        self.objects = objects

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def _on_event(self, event: pygame.event):
        self.handle_event(event)

    def draw(self):
        for obj in self.objects:
            obj.draw(self.screen)
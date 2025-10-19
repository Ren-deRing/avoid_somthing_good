from typing import TYPE_CHECKING
from abc import abstractmethod
from object import GameObject
import pygame

if TYPE_CHECKING: # Python 3.10 or less를 위한 Forward Reference Type Checking
    from manager import SceneManager

class Scene:
    # 모든 Scene은 ScreenManager에 등록되어 관리되어야 합니다.
    def __init__(self, screen: pygame.Surface, objects: list[GameObject]):
        self.screen = screen
        self.objects = objects

    def set_manager(self, manager: "SceneManager"):
        self.manager = manager

    @abstractmethod
    def update(self, dt: float):
        pass

    @abstractmethod
    def handle_event(self, event: pygame.event.Event):
        pass

    def _on_event(self, event: pygame.event.Event):
        self.handle_event(event)

    def _update(self, dt: float):
        self.update(dt)
        for obj in self.objects:
            obj._update(dt)

    def _draw(self):
        for obj in self.objects:
            obj._draw(self.screen)
from pygame.math import Vector2
from abc import abstractmethod
from typing import Type, TypeVar, cast
from component import Component
import pygame

C = TypeVar('C', bound=Component)

class GameObject:
    def __init__(self, pos: Vector2 | tuple[float, float], size: tuple[int, int],
                 texture: pygame.Surface, components: dict[Type[Component], Component] | None = None):
        self.pos = Vector2(pos)
        self.size = size
        self.texture = pygame.transform.scale(texture, size)

        if components is None:
            self.components = {}
        else:
            self.components = components
            for component in self.components.values():
                component.set_owner(self)

    def add_component(self, component: Component):
        component.set_owner(self)
        self.components[type(component)] = component

    def get_component(self, component_type: Type[C]) -> C | None:
        component = self.components.get(component_type)
        if component is not None:
            return cast(C, component)
        return None

    def get_pos(self) -> Vector2:
        return self.pos
    
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.pos.x - (self.size[0] / 2), self.pos.y - (self.size[1] / 2), *self.size)
    
    def set_pos(self, pos: Vector2 | tuple[float, float]):
        self.pos = Vector2(pos)

    def _update(self, dt: float):
        for component in self.components.values():
            component.update(dt)

    def _draw(self, screen: pygame.Surface):
        screen.blit(self.texture, Vector2(self.pos[0] - (self.size[0] / 2), self.pos[1] - (self.size[1] / 2)) )
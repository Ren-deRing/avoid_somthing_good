from pygame.math import Vector2
import pygame

class GameObject:
    def __init__(self, pos: Vector2 | tuple[float, float], size: tuple[int, int], texture: pygame.Surface):
        self.pos = Vector2(pos)
        self.size = size
        self.texture = pygame.transform.scale(texture, size)

        self.velocity: Vector2 = Vector2(0, 0)
        self.accel: Vector2 = Vector2(0, 0)

    def set_velocity(self, velocity: Vector2 | tuple[float, float]):
        self.velocity = Vector2(velocity)

    def get_velocity(self):
        return self.velocity

    def get_pos(self):
        return self.pos
    
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.pos.x), int(self.pos.y), *tuple(map(int, self.size)))
    
    def set_pos(self, pos: Vector2 | tuple[float, float]):
        self.pos = Vector2(pos)

    def set_accel(self, accel: Vector2 | tuple[float, float]):
        self.accel = Vector2(accel)

    def get_accel(self):
        return self.accel

    def _update(self, dt: float):
        self.velocity += (self.accel * dt)
        self.pos += (self.velocity * dt)

    def _draw(self, screen: pygame.Surface):
        screen.blit(self.texture, tuple(map(int, self.pos)))
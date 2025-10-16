from pygame import Surface, Vector2
from object import GameObject
import pygame

class PhysicsObject(GameObject):
    def __init__(self, pos: Vector2 | tuple[float, float], size: tuple[int, int], texture: Surface, mass: float):
        self.set_mass(mass) # mass가 0보다 작을 경우 방지
        super().__init__(pos, size, texture)

    def set_mass(self, mass: float):
        if mass > 0:
            self.mass = mass
        else:
            raise Exception('PhysicsObject의 질량이 0보다 작음.')

    def apply_force(self, force: Vector2):
        # F = ma, a = F / m
        self.accel += force / self.mass
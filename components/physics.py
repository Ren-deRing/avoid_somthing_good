from component import Component
from pygame.math import Vector2
from object import GameObject

class PhysicalComponent(Component):
    def __init__(self, mass: float, drag: float) -> None:
        self.set_mass(mass) # mass가 0보다 작을 경우 방지
        self.drag = drag
        
        self.velocity = Vector2(0, 0)
        self.accel = Vector2(0, 0)

    def set_mass(self, mass: float):
        if mass > 0:
            self.mass = mass
        else:
            raise Exception(f'PhysicalComponent의 질량이 0보다 작음.')

    def apply_force(self, force: Vector2):
        # F = ma, a = F / m
        self.accel += Vector2(force) / self.mass

    def set_velocity(self, velocity: Vector2 | tuple[float, float]):
        self.velocity = Vector2(velocity)

    def get_velocity(self):
        return self.velocity
    
    def set_accel(self, accel: Vector2 | tuple[float, float]):
        self.accel = Vector2(accel)

    def get_accel(self):
        return self.accel
    
    def update(self, dt: float):
        # F = -drag * v, 따라서 a = F / mass = -drag * v / mass
        drag_accel = -self.velocity * self.drag / self.mass
        self.accel += drag_accel
        
        self.velocity += (self.accel * dt)
        self.owner.pos += (self.velocity * dt)

        # 가속도 초기화
        self.accel = Vector2(0, 0)
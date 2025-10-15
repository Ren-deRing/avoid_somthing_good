import pygame

class GameObject:
    def __init__(self, pos: pygame.math.Vector2, size: tuple, texture: pygame.Surface):
        self.pos = pos
        self.size = size
        self.texture = pygame.transform.scale(texture, size)

    def move(self, move_vec: pygame.math.Vector2):
        self.pos += move_vec

    def handle_event(self, event):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(self.texture, self.pos)
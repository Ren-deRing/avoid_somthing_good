import pygame

def make_surface(size, color):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf
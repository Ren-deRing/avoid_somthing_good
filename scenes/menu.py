from pygame.event import Event
from scene import Scene
from object import GameObject
import colors
import utils
import pygame
import random

class MainMenu(Scene):
    def __init__(self, screen: pygame.Surface):
        self.frame = 0
        self.screen = screen

        self.playbutton = GameObject((50, 50), (50, 50), utils.make_surface((10, 10), colors.BLACK))
        self.objects = [
            GameObject((0, 0), screen.get_size(), utils.make_surface(screen.get_size(), colors.WHITE)),
            self.playbutton
        ]
        super().__init__(screen, self.objects)

    def update(self, dt: float):
        self.frame += 1
        if (self.frame % 60) == 1:
            size = self.screen.get_size()
            self.playbutton.set_pos((random.randint(0, size[0]), random.randint(0, size[1])))

    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.playbutton.get_rect().collidepoint(event.pos):
                print("Play!!")
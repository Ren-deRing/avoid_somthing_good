from stage import Stage
from object import GameObject
import colors
import utils
import pygame

class MainMenu(Stage):
    def __init__(self, screen: pygame.Surface):
        self.playbutton_region = pygame.Rect(200, 200, 10, 10)
        self.objects = [
            GameObject((0, 0), screen.get_size(), utils.make_surface(screen.get_size(), colors.WHITE)),
            GameObject((200, 200), (10, 10), utils.make_surface((10, 10), colors.BLACK))
        ]
        super().__init__(screen, self.objects)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.playbutton_region.collidepoint(event.pos):
                print("Play 버튼 클릭!")
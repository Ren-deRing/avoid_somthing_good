from pygame.event import Event
from scene import Scene
from object import GameObject
from components.physics import PhysicalComponent
import colors
import utils
import pygame

class AvoidScene(Scene):
    def __init__(self, screen: pygame.Surface):
        self.avoid_button = GameObject(pygame.Vector2(screen.get_size()) / 2, (50, 50), utils.make_surface((10, 10), colors.WHITE))
        self.avoid_button.add_component(PhysicalComponent(1.0, 1.0))
        self.objects = [ 
            GameObject(pygame.Vector2(screen.get_size()) / 2, screen.get_size(), utils.make_surface(screen.get_size(), colors.BLACK)),
            self.avoid_button
        ]
        super().__init__(screen, self.objects)

    def update(self, dt: float):
        mouse_pos = pygame.mouse.get_pos()
        direction_vector = mouse_pos - self.avoid_button.get_pos()
        distance = direction_vector.length()

        if distance < 100:
            FORCE = 50000.0
            
            # 힘은 거리에 반비례
            force_magnitude = FORCE / (distance + 1.0) 

            # 힘은 마우스에서 멀어지는 방향
            if distance > 0:
                repel_direction = -direction_vector.normalize()
            else:
                repel_direction = pygame.math.Vector2(0, 0)

            force = repel_direction * force_magnitude
            phys_comp = self.avoid_button.get_component(PhysicalComponent)
            
            if phys_comp is not None:
                phys_comp.apply_force(force)

    def draw(self):
        pygame.draw.rect(self.screen, colors.GREEN, self.avoid_button.get_rect(), 2)

    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.avoid_button.get_rect().collidepoint(event.pos):
                self.manager.remove_scene_to_render(self.__class__.__name__)
                print(self.manager.add_scene_to_render('MainMenuScene'))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                self.avoid_button.set_pos(pygame.Vector2(self.screen.get_size()) / 2)
                phys_comp = self.avoid_button.get_component(PhysicalComponent)
                if phys_comp:
                    phys_comp.set_accel((0, 0))
                    phys_comp.set_velocity((0, 0))
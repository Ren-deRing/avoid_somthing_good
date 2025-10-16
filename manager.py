from scene import Scene
import pygame

class SceneManager:
    # Scenes는 FIFO (First In First Out) 에 따라 Draw하므로, 마지막 Scene이 위에 그려집니다.
    def __init__(self, scene: list[Scene] | Scene):
        if not isinstance(scene, list):
            self.scenes = [scene]
        else: self.scenes = scene

        self.set_manager()
        self.scenes_to_remove: list[Scene] = []

    def set_manager(self):
        for s in self.scenes:
            s.set_manager(self)

    def add_scene(self, scene: list[Scene] | Scene):
        if isinstance(scene, list):
            self.scenes.extend(scene)
        else: self.scenes.append(scene)
        self.set_manager()

    # 제거로 지정된 Scene은 _update 호출 완료시에 제거됩니다.
    def remove_scene(self, scene: list[Scene] | Scene):
        if isinstance(scene, list):
            self.scenes_to_remove.extend(scene)
        else: self.scenes_to_remove.append(scene)

    def set_scene(self, scene: list[Scene] | Scene):
        if isinstance(scene, list):
            self.scenes = scene
        else: self.scenes = [scene]
        self.set_manager()

    def _on_event(self, event: pygame.event.Event):
        if len(self.scenes) > 0:
            self.scenes[-1].handle_event(event)

    def _update(self, dt: float):
        for scene in self.scenes:
            scene._update(dt)
        if self.scenes_to_remove:
            self.scenes = [s for s in self.scenes if s not in self.scenes_to_remove]
            self.scenes_to_remove.clear()

    def _draw(self):
        for scene in self.scenes:
            scene._draw()
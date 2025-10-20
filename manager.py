from typing import Type
from scene import Scene
import pygame

class SceneManager:
    # SceneManager는 FIFO (First In First Out) 에 따라 Draw하므로, 마지막 Scene이 위에 그려집니다.

    # 기본적으로 Scene은 Class 형태로 입력되어야 하며,
    # 게임에 사용될 모든 Scene은 Manager 초기화 시 입력되어야 합니다.
    # Render로 체크된 Scene은 내부에서 Instance화 되어 Render됩니다.
    def __init__(self, screen: pygame.Surface, scenes: list[Type[Scene]] | Type[Scene]):
        if not isinstance(scenes, list):
            self.scenes = [scenes]
        else: self.scenes = scenes

        self.screen = screen

        # Scenes dict 초기화
        self.scenes_dict = {}
        for scene in self.scenes:
            self.scenes_dict[scene.__name__] = scene

        self.scenes_to_render: list[Scene] = []

        self.scenes_to_remove_render: list[Scene] = []
        self.scenes_to_remove: list[Type[Scene]] = []

    def set_manager(self, scenes: list[Scene]):
        for s in scenes:
            s.set_manager(self)

    def add_scene_to_render(self, scene_name: str, *args, **kwargs) -> bool:
        if scene_name in self.scenes_dict.keys():
            if not any(s.__class__.__name__ == scene_name for s in self.scenes_to_render):
                scenes_instance = self.scenes_dict[scene_name](self.screen, *args, **kwargs)

                self.scenes_to_render.append(scenes_instance)
                self.set_manager([scenes_instance])
                return True
        return False
    
    def remove_scene_to_render(self, scene_name: str) -> bool:
        if scene_name in self.scenes_dict.keys():
            for scene_to_render in self.scenes_to_render:
                if scene_to_render.__class__.__name__ == scene_name:
                    self.scenes_to_remove_render.append(scene_to_render)
                    return True
        return False

    def add_scene(self, scene: list[Type[Scene]] | Type[Scene]):
        if isinstance(scene, list):
            self.scenes.extend(scene)
            for s in scene:
                self.scenes_dict[s.__name__] = s
        else:
            self.scenes.append(scene)
            self.scenes_dict[scene.__name__] = scene

    # 제거로 지정된 Scene은 _update 호출 완료시에 제거됩니다.
    def remove_scene(self, scene: list[Type[Scene]] | Type[Scene]):
        if isinstance(scene, list):
            self.scenes_to_remove.extend(scene)
        else: self.scenes_to_remove.append(scene)

    def set_scene(self, scene: list[Type[Scene]] | Type[Scene]):
        if isinstance(scene, list):
            self.scenes = scene
        else: self.scenes = [scene]

        self.scenes_dict.clear()
        for s in self.scenes:
            self.scenes_dict[s.__name__] = s

    def _on_event(self, event: pygame.event.Event):
        if len(self.scenes_to_render) > 0:
            self.scenes_to_render[-1].handle_event(event)

    def _update(self, dt: float):
        for scene in self.scenes_to_render: # Render로 지정된 Scene update
            scene._update(dt)

        for scene in self.scenes_to_remove_render: # Remove 플래그된 Render Scene Remove
            if scene in self.scenes_to_render:
                self.scenes_to_render.remove(scene)
        self.scenes_to_remove_render.clear()
        
        for scene_class in self.scenes_to_remove: # Remove 플래그된 Scene Remove
            if scene_class in self.scenes:
                self.scenes.remove(scene_class)
            if scene_class.__name__ in self.scenes_dict: # scenes_dict 갱신
                del self.scenes_dict[scene_class.__name__]
        self.scenes_to_remove.clear()

    def _draw(self):
        for scene in self.scenes_to_render:
            scene._draw()
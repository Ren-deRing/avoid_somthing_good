from typing import TYPE_CHECKING
from abc import abstractmethod

if TYPE_CHECKING: # Python 3.10 or less를 위한 Forward Reference Type Checking
    from object import GameObject

class Component:
    def __init__(self) -> None:
        pass

    def set_owner(self, owner: 'GameObject'):
        self.owner = owner

    @abstractmethod
    def update(self, dt: float):
        pass

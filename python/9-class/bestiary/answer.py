from dataclasses import dataclass
from weaponry.sword import Sword
from weaponry.shield import Shield
from weaponry.crossbow import Crossbow
from world.health import Health


class Knight:
    NOBLE_SWORD_NAME = "Экскалибур"

    def __init__(self, name):
        self.name = name
        self.equipment = Equipment()
        self.health = Health.give_birth_a_knight()

    def check_shield(self):
        return bool(self.equipment.shield.health)

    def loads_crossbow(self, bolts: int):
        for bolt in range(bolts):
            self.equipment.crossbow.load()

    @staticmethod
    def pronoun_an_elder(elder: str) -> str:
        return f"Мой славный предок, рыцарь {elder}"

    def __repr__(self):
        return f"Вот я — {self.name}, мой меч — {self.equipment.sword.name}!"


@dataclass
class Equipment:
    sword: Sword | None = None
    shield: Shield | None = None
    crossbow: Crossbow | None = None

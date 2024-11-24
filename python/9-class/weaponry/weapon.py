from random import randint


class Weapon:
    def __init__(self, ranged: bool, damage: int):
        self.ranged: bool = ranged  # радиус действия оружия в метрах
        self.damage: int = damage

    def deal_damage(self) -> int:
        return self.damage + randint(1, 10) - randint(1, 10)

    def shoot(self):
        if self.ranged:
            return self.deal_damage()
        else:
            return 0

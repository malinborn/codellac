from weaponry.weapon import Weapon


class Claws(Weapon):
    def double_attack(self) -> int:
        return self.deal_damage() + self.deal_damage()
        
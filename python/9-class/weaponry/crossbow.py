from weaponry.weapon import Weapon


class Crossbow(Weapon):
    def __init__(self, ranged: bool, damage: int):
        super().__init__(ranged, damage)
        self.__bolts = 0

    def deal_damage(self) -> int:
        if self.__bolts > 0:
            self.__bolts -= 1
            return super().deal_damage()
        else:
            print("😱 О нет! У рыцаря закончились болты!")
            return 0

    def load(self) -> int:
        self.__bolts += 1
        return self.__bolts

    def __len__(self):
        return self.__bolts

from weaponry.weapon import Weapon


class Sword(Weapon):
    DEFAULT_SWORD_NAME = "ну меч"
    _LEGENDARY_SWORDS_NAMES = [
        "Экскалибур",
        "Гламдринг",
        "Андуриль",
        "Штормразящий",
        "Поглотитель душ",
        "Ледяной трон",
        "Кровавый меч",
        "Дюрандаль",
        "Калибурн",
        "Масамунэ"
    ]

    def __init__(self, ranged: bool, damage: int, name: str = DEFAULT_SWORD_NAME):
        if name.lower() in [x.lower() for x in Sword._LEGENDARY_SWORDS_NAMES]:
            damage = damage + 10
        super().__init__(ranged, damage)
        self.name = name

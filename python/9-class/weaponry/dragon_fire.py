from weaponry.weapon import Weapon


class DragonFire(Weapon):
    def blaze(self):
        return self.shoot() + 5

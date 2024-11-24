from weaponry.claws import Claws
from weaponry.dragon_fire import DragonFire
from world.health import Health


class Dragon:
    def __init__(self):
        self.health: Health = Health._give_birth_a_dragon()
        self.claws: Claws = Claws(False, 10)
        self.fire: DragonFire = DragonFire(True, 10)
        self.is_flying: bool = False

    def takeoff(self):
        print()
        print("Расправив крылья, бестия взлетела! 🦇")
        print()
        self.is_flying = True

    def is_it_time_to_fly(self):
        if self.health.check() < 30:
            if not self.is_flying:
                self.takeoff()

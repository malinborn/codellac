from world.health import Health


class Shield:
    def __init__(self):
        self.health: Health = Health.give_birth_a_knight()

    def punch_is_taken(self, damage: int) -> bool:
        self.health.damaged(damage)
        return self.health.alive

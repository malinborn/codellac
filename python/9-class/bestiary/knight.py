from dataclasses import dataclass
from weaponry.sword import Sword
from weaponry.shield import Shield
from weaponry.crossbow import Crossbow
from world.health import Health


class Knight:
    pass

@dataclass
class Equipment:
    sword: Sword | None = None
    shield: Shield | None = None
    crossbow: Crossbow | None = None

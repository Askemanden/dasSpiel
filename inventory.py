from enum import IntEnum
from vectors import Vector2i

EQUIPPED_INVENTORY_POSITION : Vector2i = Vector2i(-1,-1)

class MINING_TYPE(IntEnum):
    NONE = 0
    STONE = 1
    WOOD = 2
    BUSH = 3

class Item:
    def __init__(self, inventory_position : Vector2i, equipable : bool, miningTypes : list[MINING_TYPE]):
        self.equipable = equipable
        self.miningTypes : list[MINING_TYPE] = miningTypes
        self.inventory_position = inventory_position

class Hand(Item):
    def __init__(self, inventory_position : Vector2i):
        super().__init__(inventory_position, True, [MINING_TYPE.BUSH])

class Inventory:
    def __init__(self):
        self.items : list[Item] = []
        self.equipped : Item = Hand(EQUIPPED_INVENTORY_POSITION)
        self.opened : bool = False


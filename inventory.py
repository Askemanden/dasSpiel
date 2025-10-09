from enum import IntEnum
from vectors import Vector2i

EQUIPPED_INVENTORY_POSITION : Vector2i = Vector2i(-1,-1)

class MINING_TYPE(IntEnum):
    NONE = 0
    STONE = 1
    WOOD = 2
    BUSH = 3

class Item:
    def __init__(self, equipable : bool, miningTypes : list[MINING_TYPE]):
        self.equipable = equipable
        self.miningTypes : list[MINING_TYPE] = miningTypes

class Hand(Item):
    def __init__(self):
        super().__init__(True, [MINING_TYPE.BUSH])

class StoneBlock(Item):
    def __init__(self):
        super().__init__(True, [MINING_TYPE.STONE, MINING_TYPE.WOOD])

class WoodBlock(Item):
    def __init__(self):
        super().__init__(True, [MINING_TYPE.WOOD])

class Apple(Item):
    def __init__(self):
        super().__init__(True, [MINING_TYPE.BUSH])

class Inventory:
    def __init__(self):
        self.items : list[Item] = []
        self.equipped : Item = Hand()
        self.opened : bool = False
    
    def addItem(self, item : Item):
        if item == None:
            return
        self.items.append(item)



class Item:
    def __init__(self):
        pass

class Inventory:
    def __init__(self):
        self.items : list[Item] = []
        self.opened : bool = False
        


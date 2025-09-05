from collections.abc import Callable

class Signal:
    def __init__(self):
        self.connections : dict[str, Callable[[list], None]] = {}

    def connect(self, name : str, func : Callable[[list], None]):
        self.connections[name] = func

    def remove(self, name : str):
        self.connections.pop(name, 1)
    
    def emit(self, params : list):
        for key in self.connections.keys():
            self.connections[key](params)

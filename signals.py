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

if __name__ == "__main__":
    signal1 = Signal()

    def testfunc1(params : list):
        print(params)
    
    def testfunc2(params : list):
        for param in params:
            print(param)
    
    signal1.connect("testfunc1", testfunc1)
    signal1.connect("testfunc2", testfunc2)

    signal1.emit([1,2,"dumdum",(3,2,"AAA-Batteri")])
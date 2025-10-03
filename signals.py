from collections.abc import Callable

class Signal:
    def __init__(self):
        self.connections : list[list[str, Callable[[list], bool]]] = []

    def connect(self, name : str, func : Callable[[list], bool]):
        self.connections.append([name,func])

    def remove(self, name : str):
        for i in self.connections:
            if i[0] == name:
                self.connections.remove(i)
                break
    
    def emit(self, params : list):
        for connection in self.connections:
            consumed = connection[1](params)
            if(consumed):
                break

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
import math

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def change_values(self, x, y):
        self.x = x
        self.y = y

    def change_values(self, other : "Vector2") -> None:
        self.change_values(other.x, other.y)
    
    def length(self) -> float:
        return math.sqrt(self.x**2+self.y**2)
    
    def __add__(self, other : "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other : "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __truediv__(self, scalar : float) -> "Vector2":
        return Vector2(self.x/scalar, self.y/scalar)
    
    def __mul__(self, scalar : float) -> "Vector2":
        return Vector2(self.x*scalar, self.y*scalar)

    def __iadd__(self, other : "Vector2"):
        result = self + other
        self.change_values(result.x, result.y)
        return self
    
    def __itruediv__(self, scalar : float):
        self.change_values(self/scalar)
        return self
    
    def __isub__(self, other : "Vector2"):
        self.change_values(self - other)
        return self

    def __imul__(self, scalar : float):
        self.change_values(self * scalar)
        return self
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, other):
        return isinstance(other, Vector2) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x,self.y))

class Vector2f(Vector2):
    
    def __init__(self, x : float, y : float):
        super().__init__(x, y)

class Vector2i(Vector2):

    def __init__(self, x : int, y : int):
        super().__init__(x, y)
    
    def change_values(self, x : int, y : int):
        self.x = int(x)
        self.y = int(y)
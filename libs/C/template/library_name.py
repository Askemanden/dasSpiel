import ctypes

lib = ctypes.CDLL('./library_name.so')

lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

def add(a, b):
    return lib.add(a, b)

lib.mult.argtypes = [ctypes.c_double, ctypes.c_double]
lib.mult.restype = ctypes.c_double

def mult(a, b):
    return lib.mult(a, b)


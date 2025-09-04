# This version only supports double
# import re

# library_name = "library_name"

# def parse_header(header_file):
#     with open(header_file, 'r') as f:
#         code = f.read()

#     pattern = r'(\w[\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)\s*;'
#     matches = re.findall(pattern, code)

#     functions = []
#     for ret_type, name, args in matches:
#         arg_names = [arg.strip().split()[-1] for arg in args.split(',') if arg.strip()]
#         arg_types = ['ctypes.c_double'] * len(arg_names)  # Simplified: assumes all args are double
#         functions.append((name, arg_names, arg_types))
#     return functions

# def generate_wrapper(functions, lib_name, output_file):
#     with open(output_file, 'w') as f:
#         f.write("import ctypes\n\n")
#         f.write(f"lib = ctypes.CDLL('./{lib_name}.so')\n\n")

#         for name, arg_names, arg_types in functions:
#             f.write(f"lib.{name}.argtypes = [{', '.join(arg_types)}]\n")
#             f.write(f"lib.{name}.restype = ctypes.c_double\n\n")
#             f.write(f"def {name}({', '.join(arg_names)}):\n")
#             f.write(f"    return lib.{name}({', '.join(arg_names)})\n\n")

# if __name__ == "__main__":
#     funcs = parse_header(f"{library_name}.h")
#     generate_wrapper(funcs, f"{library_name}", f"{library_name}.py")

import re
import ctypes

library_name = "library_name"

# Mapping C types to ctypes
ctype_map = {
    'int': 'ctypes.c_int',
    'float': 'ctypes.c_float',
    'double': 'ctypes.c_double',
    'char': 'ctypes.c_char',
    'char*': 'ctypes.c_char_p',
    'bool': 'ctypes.c_bool',
    'void': 'None',
    'void*': 'ctypes.c_void_p',
    'long': 'ctypes.c_long',
    'short': 'ctypes.c_short',
    'unsigned int': 'ctypes.c_uint',
    'unsigned char': 'ctypes.c_ubyte',
    'unsigned long': 'ctypes.c_ulong',
    'unsigned short': 'ctypes.c_ushort',
    'size_t': 'ctypes.c_size_t',
}

def normalize_type(c_type):
    c_type = c_type.strip().replace('const', '').replace('unsigned', 'unsigned ').replace('  ', ' ')
    return ctype_map.get(c_type, 'ctypes.c_void_p')  # fallback to void pointer

def parse_header(header_file):
    with open(header_file, 'r') as f:
        code = f.read()

    pattern = r'([\w\s\*\d]+)\s+(\w+)\s*\(([^)]*)\)\s*;'
    matches = re.findall(pattern, code)

    functions = []
    for ret_type, name, args in matches:
        arg_list = []
        arg_names = []
        if args.strip() != 'void':
            for arg in args.split(','):
                parts = arg.strip().split()
                if len(parts) >= 2:
                    arg_type = ' '.join(parts[:-1])
                    arg_name = parts[-1]
                    arg_list.append(normalize_type(arg_type))
                    arg_names.append(arg_name)
        functions.append((name, arg_names, arg_list, normalize_type(ret_type)))
    print(functions)
    return functions

def generate_wrapper(functions, lib_name, output_file):
    with open(output_file, 'w') as f:
        f.write("import ctypes\n\n")
        f.write(f"lib = ctypes.CDLL('./{lib_name}.so')\n\n")

        for name, arg_names, arg_types, ret_type in functions:
            f.write(f"lib.{name}.argtypes = [{', '.join(arg_types)}]\n")
            f.write(f"lib.{name}.restype = {ret_type}\n\n")
            f.write(f"def {name}({', '.join(arg_names)}):\n")
            f.write(f"    return lib.{name}({', '.join(arg_names)})\n\n")

if __name__ == "__main__":
    funcs = parse_header(f"{library_name}.h")
    generate_wrapper(funcs, f"{library_name}", f"{library_name}.py")



def divide(a, b):
    if b <= 0:
        raise ValueError(f"b={b} doit etre plus grand que 0")
    else:
        return a/b
    
print(divide(10, 2))
print(divide(10, -1))
print(divide(10, 0))
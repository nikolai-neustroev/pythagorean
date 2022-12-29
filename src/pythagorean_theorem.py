def hypotenuse(a, b):
    if a > 0 and b > 0:
        c = (a**2 + b**2)**0.5
        return c
    else:
        raise ValueError("a, b must be positive, try again")

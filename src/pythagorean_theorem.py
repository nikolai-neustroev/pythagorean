def hypotenuse(a: float, b: float):
    if a > 0.0 and b > 0.0:
        c = (a**2 + b**2)**0.5
        return c
    else:
        raise ValueError("a, b must be positive, try again")

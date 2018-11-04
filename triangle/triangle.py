def is_triangle(sides):
    return len(sides) == 3 and sum(sides) > 2 * max(sides)

def is_equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def is_isosceles(sides):
    return is_triangle(sides) and not is_scalene(sides)

def is_scalene(sides):
    return is_triangle(sides) and len(sides) == len(set(sides))

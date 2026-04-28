import math

def is_perfect_square(n):
    root = int(math.isqrt(n))
    return root * root == n

def find_first_square(base):
    root = int(math.isqrt(base)) + 1
    if root % 2 != base % 2:
        root += 1
    current = root * root
    while (current - base) % 36 != 0:
        root += 2
        current = root * root
    return current

def find_square(n):
    a_squared = ((n + 1) // 2) ** 2
    floor = a_squared % 36
    current = floor if floor > 0 else 36
    if not is_perfect_square(current):
        current = find_first_square(current)
    stop = 2 * n
    steps = 0
    
    while current < stop:
        if current >= n and is_perfect_square(current) and is_perfect_square(current - n):
            c = int(math.isqrt(current))
            d = int(math.isqrt(current - n))
            f1 = c + d
            f2 = c - d
            print(f"N = {n}, Found square: {current}, root = {c}, steps = {steps}")
            print(f"C = {c}, D = {d}, F1 = {f1}, F2 = {f2}")
            return
        current += 36
        steps += 1
    
    print(f"N = {n}, No square found within bounds.")

find_square(77)
find_square(35)
find_square(143)
find_square(493)
find_square(10403)
find_square(821539)

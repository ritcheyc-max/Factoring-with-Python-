import math

def is_perfect_square(n):
    root = int(math.isqrt(n))
    return root * root == n

def find_square(n):
    a_squared = ((n + 1) // 2) ** 2
    floor = a_squared % 36
    current = floor if floor > 0 else 36
    stop = 2 * n
    steps = 0
    
    while current < stop:
        if current >= n and is_perfect_square(current) and is_perfect_square(current - n):
            print(f"N = {n}, Found square: {current}, root = {int(math.isqrt(current))}, steps = {steps}")
            return
        current += 36
        steps += 1
    
    print(f"N = {n}, No square found within bounds.")

find_square(77)
find_square(35)
find_square(143)
find_square(493)

import math
def math_calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(math.sqrt(a**10 + b**10))

a, b = int(input()), int(input())
math_calc(a, b)
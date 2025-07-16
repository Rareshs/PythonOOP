import math


def calculate_pow(a: int, b: int) -> float:
    return math.pow(a, b)


def calculate_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

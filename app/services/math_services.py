import math
import time
from functools import lru_cache, wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}{args}{' '+str(kwargs) if kwargs else ''} → {elapsed:.6f}s")
        return result
    return wrapper


@timeit
def calculate_pow(a: int, b: int) -> float:
    return math.pow(a, b)


@timeit
@lru_cache(maxsize=None)
def calculate_fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@timeit
def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

# Use Ctrl + I to write some Python code
# Your instruction to the chatbot will be
# I am an amateur number theorist, and I am curious about special sequences of numbers. 
# I would like to write a couple of Python functions that tell me the following: 
# the nth number in the Fibonacci sequence, and the first ten prime numbers.

from math import isqrt
from typing import List

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number with fibonacci(0)=0, fibonacci(1)=1 (n >= 0)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(k: int) -> bool:
    """Simple primality check for k >= 2."""
    if k < 2:
        return False
    if k % 2 == 0:
        return k == 2
    r = isqrt(k)
    for d in range(3, r + 1, 2):
        if k % d == 0:
            return False
    return True

def first_ten_primes() -> List[int]:
    """Return a list of the first ten prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < 10:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

if __name__ == "__main__":
    # Example usage
    print("Fibonacci(0..10):", [fibonacci(i) for i in range(11)])
    print("First ten primes:", first_ten_primes())
# Use AI to document some Python code.

# Put your cursor on a function.
# It is possible that the AI will suggest a docstring,
# which you can accept via tab-complete.
# You can also edit the docstring as needed.
# If the AI is not suggesting something,
# use Ctrl + I to invoke the AI to suggest a docstring,
# or start typing """ which will clue it in to suggest a docstring.

# At the bottom of the file,
# use Ctrl + I to write example usages of the functions,
# or start typing if __name__ == "__main__": 
# which will clue it in to suggest example usages.

from math import comb, isqrt
from typing import List

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(k):
    if k < 2:
        return False
    if k % 2 == 0:
        return k == 2
    r = isqrt(k)
    for d in range(3, r + 1, 2):
        if k % d == 0:
            return False
    return True

def first_ten_primes():
    primes = []
    candidate = 2
    while len(primes) < 10:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes
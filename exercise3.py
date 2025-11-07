# Use Ctrl + I to rewrite some Python code with different approaches
# Your instruction to the chatbot will be
# I am an amateur number theorist, and I know that are multiple ways to generate prime numbers.
# I wrote a simple function to generate prime numbers, which is highlighted, but I would like to see an alternative implementation.
# Specifically, I would like you to write two functions that use the sieves of Eratosthenes and Atkin to generate prime numbers.

# Next, we will check that both implementations produce the same first ten prime numbers.
# Your instruction to the chatbot will be
# Please write two functions that generate the first ten prime numbers with either the sieves of Atkin or Eratosthenes. 
# Write the if __name__ == "__main__" code to verify that the two sieve implementations provide the same first ten prime numbers.

from math import comb, isqrt
from typing import List

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
    print("First ten primes:", first_ten_primes())
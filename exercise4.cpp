// Use Ctrl + I to translate some Python code into R code
// Notice that in this script, we do not have the same linter coloring
// as in Python scripts because these are Python code snippets inside
// a C++ script. However, the chatbot will be able to translate the code.

// Your instruction to the chatbot will be
// I am an experienced Python programmer, and therefore implemented my code in Python.
// However, I have collaborators who prefer C++ because it can be faster or more memory efficient.
// Please translate the following Python code into C++ code.


from math import isqrt
from typing import List

def sieve_eratosthenes(limit: int) -> List[int]:
    """Return all primes <= limit using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start: limit + 1: step] = b'\x00' * (((limit - start) // step) + 1)
    return [i for i, isprime in enumerate(sieve) if isprime]

def sieve_atkin(limit: int) -> List[int]:
    """Return all primes <= limit using the Sieve of Atkin."""
    if limit < 2:
        return []
    sieve = [False] * (limit + 1)
    r = isqrt(limit)
    for x in range(1, r + 1):
        xx = x * x
        for y in range(1, r + 1):
            yy = y * y
            n = 4 * xx + yy
            if n <= limit and n % 12 in (1, 5):
                sieve[n] = not sieve[n]
            n = 3 * xx + yy
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * xx - yy
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    primes = []
    if limit >= 2:
        primes.append(2)
    if limit >= 3:
        primes.append(3)
    for i in range(5, r + 1):
        if sieve[i]:
            step = i * i
            for k in range(step, limit + 1, step):
                sieve[k] = False
    for i in range(5, limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def first_ten_primes_eratosthenes() -> List[int]:
    """Return the first ten primes using the Sieve of Eratosthenes."""
    limit = 30
    primes = sieve_eratosthenes(limit)
    while len(primes) < 10:
        limit *= 2
        primes = sieve_eratosthenes(limit)
    return primes[:10]

def first_ten_primes_atkin() -> List[int]:
    """Return the first ten primes using the Sieve of Atkin."""
    limit = 30
    primes = sieve_atkin(limit)
    while len(primes) < 10:
        limit *= 2
        primes = sieve_atkin(limit)
    return primes[:10]

if __name__ == "__main__":
    erat_primes = first_ten_primes_eratosthenes()
    atkin_primes = first_ten_primes_atkin()
    print("Eratosthenes first ten primes:", erat_primes)
    print("Atkin       first ten primes:", atkin_primes)
    print("Match:", erat_primes == atkin_primes)
    # Optional: raise if they differ
    assert erat_primes == atkin_primes, "The two sieves produced different results"
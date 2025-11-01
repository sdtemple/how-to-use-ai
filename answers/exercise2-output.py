from math import comb, isqrt
from typing import List

def catalan(n: int) -> int:
    """
    Compute the nth Catalan number.

    Parameters
    ----------
    n : int
        Non-negative integer index (n >= 0).

    Returns
    -------
    int
        The nth Catalan number.

    Examples:
    >>> catalan(0)
    1
    >>> catalan(1)
    1
    >>> catalan(2)
    2
    >>> catalan(3)
    5
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return comb(2 * n, n) // (n + 1)

def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number.

    Parameters
    ----------
    n : int
        Non-negative integer index (n >= 0).

    Returns
    -------
    int
        The nth Fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(10)
    55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(k: int) -> bool:
    """
    Check if a number is prime.

    Parameters
    ----------
    k : int
        The number to check for primality.

    Returns
    -------
    bool
        True if k is prime, False otherwise.

    Examples:
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(17)
    True
    >>> is_prime(91)
    False
    >>> is_prime(97)
    True
    """
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
    """
    Generate a list of the first ten prime numbers.

    Parameters
    ----------
    None

    Returns
    -------
    List[int]
        A list containing the first ten prime numbers.
    """
    primes = []
    candidate = 2
    while len(primes) < 10:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

if __name__ == "__main__":
    # Example usages of the functions
    print("5th Catalan number:", catalan(5))
    print("10th Fibonacci number:", fibonacci(10))
    print("Is 97 prime?", is_prime(97))
    print("First ten prime numbers:", first_ten_primes())

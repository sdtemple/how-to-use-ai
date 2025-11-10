# Adjust how many tokens the AI uses to write code
# As of today, GitHub Copilot does not allow direct control of the number of tokens used
# in code completions. However, you can influence the length of the generated code
# by providing more or less context in your comments and code.

# Disclaimer: I did not check the correctness of the following implementations.
# They are provided as examples of varying verbosity.


# Using AI (Ctrl + I), write a very verbose function to compute prime numbers with the sieve of Eratosthenes
# Try to get it meticulously documented and long-winded.

def sieve_of_eratosthenes_verbose(n):
    """
    Compute all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    
    The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers
    up to a given limit. It works by iteratively marking the multiples of each prime
    number as composite (not prime), starting with the smallest prime number, 2.
    
    The algorithm works as follows:
    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n)
    2. Start with the first number in the list (2)
    3. Mark all multiples of 2 (except 2 itself) as composite
    4. Find the next number in the list that hasn't been marked as composite
    5. Repeat steps 3-4 until you've processed all numbers up to sqrt(n)
    6. All remaining unmarked numbers are prime
    
    Args:
        n (int): The upper limit to find primes up to (inclusive)
    
    Returns:
        list: A list of all prime numbers from 2 to n (inclusive)
    
    Examples:
        >>> sieve_of_eratosthenes_verbose(10)
        [2, 3, 5, 7]
        
        >>> sieve_of_eratosthenes_verbose(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        
        >>> sieve_of_eratosthenes_verbose(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        >>> sieve_of_eratosthenes_verbose(2)
        [2]
        
        >>> sieve_of_eratosthenes_verbose(1)
        []
        
        >>> sieve_of_eratosthenes_verbose(0)
        []
        
        >>> sieve_of_eratosthenes_verbose(100)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    
    # Handle edge cases: if n is less than 2, there are no primes
    if n < 2:
        return []
    
    # Create a boolean list "is_prime" and initialize all entries as True
    # is_prime[i] will be False if i is not a prime, else True
    # We create a list of size (n+1) so we can use indices that match the actual numbers
    is_prime = []
    for i in range(n + 1):
        is_prime.append(True)
    
    # 0 and 1 are not prime numbers by definition
    is_prime[0] = False
    is_prime[1] = False
    
    # Start with the smallest prime number, which is 2
    current_number = 2
    
    # We only need to check numbers up to the square root of n
    # This is because if n has a factor greater than sqrt(n), 
    # it must also have a factor less than sqrt(n)
    while current_number * current_number <= n:
        
        # If current_number is still marked as prime
        if is_prime[current_number]:
            
            # Mark all multiples of current_number as composite (not prime)
            # We start from current_number^2 because all smaller multiples
            # have already been marked by smaller primes
            multiple = current_number * current_number
            
            # Mark all multiples of current_number starting from current_number^2
            while multiple <= n:
                is_prime[multiple] = False  # This number is composite
                multiple = multiple + current_number  # Move to next multiple
        
        # Move to the next number to check
        current_number = current_number + 1
    
    # Collect all numbers that are still marked as prime
    primes = []
    for number in range(2, n + 1):
        if is_prime[number]:  # If this number wasn't marked as composite
            primes.append(number)  # Add it to our list of primes
    
    return primes



# Using AI (Ctrl + I), write a reasonably concise function to compute prime numbers with the sieve of Eratosthenes
# Try to get it to the point and not too verbose but clear and with comments when appropriate.


def sieve_of_eratosthenes(n):
    """
    Compute all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    
    The Sieve of Eratosthenes efficiently finds all primes up to a given number by
    systematically eliminating composite numbers. It works by marking multiples of
    each prime starting from 2, leaving only the primes unmarked.
    
    Args:
        n (int): The upper limit to find primes up to (inclusive)
    
    Returns:
        list: A list of all prime numbers from 2 to n (inclusive)
    """
    if n < 2:
        return []
    
    # Initialize boolean array - True means potentially prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve process: mark multiples as composite
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i starting from i²
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # Collect all numbers still marked as prime
    return [num for num in range(2, n + 1) if is_prime[num]]


# Using AI (Ctrl + I), write an extremely concise function to compute prime numbers with the sieve of Eratosthenes
# Try to get it as short as possible while still being correct.
# Minimize comments and documentation.
# Hint: use list comprehensions and built-in functions where possible.
# Hint: ask it to write lines with semicolons to put multiple statements on one line.

def sieve(n):
    if n < 2: return []
    s = [True] * (n + 1); s[0] = s[1] = False
    [s.__setitem__(j, False) for i in range(2, int(n**0.5) + 1) if s[i] for j in range(i*i, n + 1, i)]
    return [i for i in range(2, n + 1) if s[i]]



import math

# Use AI to debug your code

# Using the hot-key `Ctrl + I`, I instructed the AI to write some buggy code.
# The instruction to the chatbot was:
# Please write Python code that makes a function to compute the nth Catalan number 
# but the function makes a mistake and outputs the wrong number.
# Also, please write a function to compute the nth Fibonacci number
# but the function makes a mistake which creates an error.
# At the end of the file, write a if __name__ == "__main__": block
# that calls both functions with example inputs and prints the results.

# There are two functions below with bugs in them.
# Your task is to use debugging techniques to find and fix the bugs.
# Highlight the code below and use `Ctrl + I` to ask the AI to help you debug it.

def catalan(n):
    # Bug: divides by n instead of (n + 1), producing wrong results for n > 0
    # GitHub Copilot identified this and suggested this fix.
    if n == 0:
        return 1
    return math.comb(2 * n, n) // (n + 1)

def fibonacci(n):
    # Bug: second element is a string, causing a TypeError when n >= 2
    # GitHub Copilot identified this and suggested this fix.
    seq = [0, 1]
    for i in range(2, n + 1):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq[n]

if __name__ == "__main__":
    print("Catalan(5):", catalan(5))
    print("Fibonacci(10):", fibonacci(10))

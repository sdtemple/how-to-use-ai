# Use AI to refactor code
# The following code has very verbose variable names and redundant typecasting.
# It also uses a while loop instead of a for loop, which can be less efficient
# and create potential for infinite loops if not handled carefully.
# Your task is to use an AI chatbot to refactor this code to be more concise
# and efficient while maintaining the same functionality.

# Highlight over the code blocks below, then open the AI chatbot interface
# (Ctrl + I) and instruct the chatbot to refactor the code to avoid typecasting,
# poor variable names, and the use of while loops.

def fibonacci(n):
    """Calculate the nth Fibonacci number.
    
    Args:
        n (int): Position in the Fibonacci sequence (non-negative).
        
    Returns:
        int: The Fibonacci number at position n.
    """
    # Handle base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Calculate Fibonacci using iteration
    prev = 0
    curr = 1
    
    for i in range(2, n + 1):
        next_val = prev + curr
        prev = curr
        curr = next_val
    
    return curr

if __name__ == "__main__":
    print("Fibonacci sequence:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

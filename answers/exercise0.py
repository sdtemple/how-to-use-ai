# Use Ctrl + I to write some Python code
# Your instruction to the chatbot will be
# Suppose I have never coded in Python at all. 
# We will write simple functions to compute the mean and standard deviation
# from a list of numbers.

# just in case
import math
import numpy

# First, start typing "def compute_mean_v1(numbers):"
# and look for an AI-generated suggestion to complete the function.
# Click Tab to accept the suggestion.

def compute_mean_v1(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# If no suggestion to compute the standard deviation appears,
# start typing "def compute_stddev_v1(numbers):"
# and look for an AI-generated suggestion to complete the function.
# Click Tab to accept the suggestion.

def compute_stddev_v1(numbers):
    if len(numbers) == 0:
        return 0
    mean = compute_mean_v1(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5


# Second, click "Ctrl + I" to open the AI chatbot interface.
# Type the following instruction to the chatbot:
# "Can you write some code that computes the mean and standard deviation
# of the list of numbers? Name these functions compute_mean_v2 and compute_stddev_v2."
# Click "Send" to get the chatbot's response.

def compute_mean_v2(numbers):
    if not numbers:
        return 0.0
    total = 0.0
    cnt = 0
    for x in numbers:
        total += x
        cnt += 1
    return total / cnt

def compute_stddev_v2(numbers):
    if not numbers:
        return 0.0
    mu = compute_mean_v2(numbers)
    sq_sum = 0.0
    for x in numbers:
        d = x - mu
        sq_sum += d * d
    variance = sq_sum / len(numbers)
    return math.sqrt(variance)


# Third, type the same instructions to the chatbot:
# "Can you write some code that computes the mean and standard deviation
# of the list of numbers? Name these functions compute_mean_v3 and compute_stddev_v3."
# Click "Send" to get the chatbot's response.
# How did the chatbot's example code differ?
# LLMs are a model with stochastic elements, 
# so you may get different responses each time.

def compute_mean_v3(numbers):
    """Return the mean of numbers (0.0 for empty input)."""
    if not numbers:
        return 0.0
    return float(sum(numbers)) / len(numbers)

def compute_stddev_v3(numbers):
    """Return the population standard deviation (divide by n)."""
    if not numbers:
        return 0.0
    mu = compute_mean_v3(numbers)
    variance = sum((x - mu) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


# Fourth, slightly modify the instruction to the chatbot:
# "I am a slightly more experienced Python programmer.
# Can you write some example code that computes the mean and standard deviation
# of the list of numbers? Please use numpy for the calculations, but do not
# explicitly call the numpy.mean and numpy.std functions.
# Name these functions compute_mean_v4 and compute_stddev_v4."
# Click "Send" to get the chatbot's response.

def compute_mean_v4(numbers):
    """Compute the mean using numpy vectorized operations (no numpy.mean)."""
    arr = numpy.asarray(numbers, dtype=float)
    if arr.size == 0:
        return 0.0
    return float(numpy.sum(arr) / arr.size)

def compute_stddev_v4(numbers):
    """Compute the population standard deviation using numpy ops (no numpy.std)."""
    arr = numpy.asarray(numbers, dtype=float)
    if arr.size == 0:
        return 0.0
    mu = compute_mean_v4(arr)
    variance = numpy.sum((arr - mu) ** 2) / arr.size
    return float(numpy.sqrt(variance))


# Fifth, play around with different chatbots. Use the toggle dropdown menu
# in the chatbot interface (Ctrl + I) to select different LLMs.
# How do the responses differ among the various LLMs?
# Try the same instruction with different LLMs and see how the code varies.
# "Can you write some code that computes the mean and standard deviation
# of the list of numbers? Name these functions compute_mean_v5 and compute_stddev_v5."
# How did the chatbot's example code differ?
# LLMs can be parameterized differently, 
# so you may get different responses from each.

def compute_mean_v5(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def compute_stddev_v5(numbers):
    """Calculate the population standard deviation of a list of numbers."""
    if not numbers:
        return 0
    mean = compute_mean_v5(numbers)
    squared_differences = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_differences) / len(numbers)
    return math.sqrt(variance)


# Sixth, we will write a much more verbose instruction to the chatbot.
# Open the chatbot interface (Ctrl + I) and type the following instruction:
# "Can you write some code that computes the mean and standard deviation
# of the list of numbers? I know nothing about Python, so I would like
# you to explain each step of the process. I also know very little about
# statistics, so please explain what the mean and standard deviation are.
# Please include comments in the code to explain what each line does.
# Name these functions compute_mean_v6 and compute_stddev_v6."
# How did the chatbot's example code differ?
# LLMs typically provide longer responses if your instruction is more detailed.
# Roughly, the number of words are referred to as "tokens" in LLM terminology. 


def compute_mean_v6(numbers):
    """
    Calculate the mean (average) of a list of numbers.
    
    The mean is the sum of all numbers divided by how many numbers there are.
    For example, the mean of [2, 4, 6] is (2+4+6)/3 = 4.
    """
    # First, check if the list is empty to avoid division by zero
    if not numbers:  # This checks if the list has no items
        return 0  # Return 0 for empty lists
    
    # Calculate the sum of all numbers in the list
    total = sum(numbers)  # sum() adds up all the numbers
    
    # Count how many numbers are in the list
    count = len(numbers)  # len() tells us the length of the list
    
    # Divide the total by the count to get the average
    mean = total / count
    
    return mean  # Return the calculated mean


def compute_stddev_v6(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    Standard deviation measures how spread out the numbers are from the average.
    - Small standard deviation = numbers are close to the mean
    - Large standard deviation = numbers are spread far from the mean
    """
    # First, check if the list is empty
    if not numbers:  # This checks if the list has no items
        return 0  # Return 0 for empty lists
    
    # Step 1: Calculate the mean using our previous function
    mean = compute_mean_v6(numbers)
    
    # Step 2: Find how far each number is from the mean, then square those distances
    squared_differences = []  # Create an empty list to store results
    for number in numbers:  # Look at each number in our list one by one
        difference = number - mean  # How far is this number from the mean?
        squared_difference = difference ** 2  # Square it (multiply by itself)
        squared_differences.append(squared_difference)  # Add to our list
    
    # Step 3: Calculate the average of these squared differences (this is called variance)
    variance = sum(squared_differences) / len(numbers)
    
    # Step 4: Take the square root of variance to get standard deviation
    standard_deviation = math.sqrt(variance)  # sqrt means square root
    
    return standard_deviation  # Return the calculated standard deviation


# Finally, a best practice is to ask the chatbot to test the code it wrote.
# In this case, we asked the chatbot to write the same functions multiple times.
# Below, I wrote code to print to terminal the results from each version of the functions.
# You will run "python exercise0.py" in a terminal to see the results.
# We enter the terminal with "Ctrl + `

if __name__ == "__main__":
    test_numbers = [10, 20, 30, 40, 50]
    
    mean_v1 = compute_mean_v1(test_numbers)
    stddev_v1 = compute_stddev_v1(test_numbers)
    
    mean_v2 = compute_mean_v2(test_numbers)
    stddev_v2 = compute_stddev_v2(test_numbers)
    
    mean_v3 = compute_mean_v3(test_numbers)
    stddev_v3 = compute_stddev_v3(test_numbers)
    
    mean_v4 = compute_mean_v4(test_numbers)
    stddev_v4 = compute_stddev_v4(test_numbers)
    
    mean_v5 = compute_mean_v5(test_numbers)
    stddev_v5 = compute_stddev_v5(test_numbers)

    mean_v6 = compute_mean_v6(test_numbers)
    stddev_v6 = compute_stddev_v6(test_numbers)
    
    print("Mean Results:")
    print(f"v1: {mean_v1}, v2: {mean_v2}, v3: {mean_v3}, v4: {mean_v4}, v5: {mean_v5}, v6: {mean_v6}")

    print("Standard Deviation Results:")
    print(f"v1: {stddev_v1}, v2: {stddev_v2}, v3: {stddev_v3}, v4: {stddev_v4}, v5: {stddev_v5}, v6: {stddev_v6}")





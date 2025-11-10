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





# If no suggestion to compute the standard deviation appears,
# start typing "def compute_stddev_v1(numbers):"
# and look for an AI-generated suggestion to complete the function.
# Click Tab to accept the suggestion.





# Second, click "Ctrl + I" to open the AI chatbot interface.
# Type the following instruction to the chatbot:
# "Can you write some code that computes the mean and standard deviation
# of the list of numbers? Name these functions compute_mean_v2 and compute_stddev_v2."
# Click "Send" to get the chatbot's response.





# Third, type the same instructions to the chatbot:
# "Can you write some code that computes the mean and standard deviation
# of the list of numbers? Name these functions compute_mean_v3 and compute_stddev_v3."
# Click "Send" to get the chatbot's response.
# How did the chatbot's example code differ?
# LLMs are a model with stochastic elements, 
# so you may get different responses each time.





# Fourth, slightly modify the instruction to the chatbot:
# "I am a slightly more experienced Python programmer.
# Can you write some example code that computes the mean and standard deviation
# of the list of numbers? Please use numpy for the calculations, but do not
# explicitly call the numpy.mean and numpy.std functions.
# Name these functions compute_mean_v4 and compute_stddev_v4."
# Click "Send" to get the chatbot's response.







# Fifth, play around with different chatbots. Use the toggle dropdown menu
# in the chatbot interface (Ctrl + I) to select different LLMs.
# How do the responses differ among the various LLMs?
# Try the same instruction with different LLMs and see how the code varies.
# Use "Name these functions compute_mean_v5 and compute_stddev_v5."
# How did the chatbot's example code differ?
# LLMs can be parameterized differently, 
# so you may get different responses from each.







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



# Use AI to refactor code
# The following code has very verbose variable names and redundant typecasting.
# It also uses a while loop instead of a for loop, which can be less efficient
# and create potential for infinite loops if not handled carefully.
# Your task is to use an AI chatbot to refactor this code to be more concise
# and efficient while maintaining the same functionality.

# Highlight over the code blocks below, then open the AI chatbot interface
# (Ctrl + I) and instruct the chatbot to refactor the code to avoid typecasting,
# poor variable names, and the use of while loops.

def compute_fibonacci_number_at_specified_position_in_sequence(position_index_for_fibonacci_calculation):
    """
    Computes the nth Fibonacci number using verbose variable names and redundant typecasting
    """
    # Initialize variables with confusing names
    previous_fibonacci_value_before_current = float(0)
    current_fibonacci_value_in_sequence = float(1)
    current_iteration_counter_variable = int(float(0))
    target_position_converted_to_integer = int(float(position_index_for_fibonacci_calculation))
    
    # Handle base cases
    if int(float(target_position_converted_to_integer)) <= int(float(0)):
        return int(float(0))
    elif int(float(target_position_converted_to_integer)) == int(float(1)):
        return int(float(1))
    
    # Use while loop instead of for loop
    while int(float(current_iteration_counter_variable)) < int(float(target_position_converted_to_integer)) - int(float(1)):
        temporary_storage_for_next_fibonacci_value = float(int(previous_fibonacci_value_before_current)) + float(int(current_fibonacci_value_in_sequence))
        previous_fibonacci_value_before_current = float(int(current_fibonacci_value_in_sequence))
        current_fibonacci_value_in_sequence = float(int(temporary_storage_for_next_fibonacci_value))
        current_iteration_counter_variable = int(float(current_iteration_counter_variable)) + int(float(1))
    
    return int(float(current_fibonacci_value_in_sequence))
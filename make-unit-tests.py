import doctest
import exercise2
from exercise2 import catalan
import exercise2

if __name__ == "__main__":
    
    # Run the doctests in exercise2copy.py
    results = doctest.testmod(exercise2, report=True)
    print()
    print('Testing the entire module:')
    print(results)
    print()
    print('-----------------------------------')
    print()

    # Run the doctests for the catalan function
    results = doctest.run_docstring_examples(
        catalan, # change this
        globals(),
        verbose=True
    )
    print('Testing the catalan function:')
    print(results)
    print()
    print()
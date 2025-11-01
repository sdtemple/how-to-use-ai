# How to Use AI in Coding

This repository contributes to a tutorial on how (and how not to) use AI for coding assistance. We will provide some starter code which comprise of various exercises.

---

First, suppose I am inexperienced at writing Markdown (this .md file). We will build this README file with AI. The hot key `Ctrl + I` is your friend! You enter an environment where you can ask an AI chatboat to help you write code. I made the following query in the chatbot box.

```
Can you write a Markdown enumerated list with titles Exercise 1, Exercise 2, up to Exercises 5 and explicit links to python files titled exercise1.py, exercise2.py, up to exercise5.py?
```

1. Exercise 1 — [exercise1.py](./exercise1.py)
2. Exercise 2 — [exercise2.py](./exercise2.py)
3. Exercise 3 — [exercise3.py](./exercise3.py)
4. Exercise 4 — [exercise4.py](./exercise4.py)
5. Exercise 5 — [exercise5.py](./exercise5.py)

---
Second, suppose I am an inexperienced Python coder. I created a file called [exercise1.py](./exercise1.py). Then, I made a query in the `Ctrl + I` box about writing a few functions.

```
I am an amateur number theorist, and I am curious about special sequences of numbers. I would like to write a few Python functions that tell me the nth Catalan number, the nth number in the Fibonnaci sequence, and the first ten prime numbers.
```

The chatbot wrote 45 lines of code that I accepted. At the bottom of the script, it provided the following code that will output some examples to the Terminal.

```
if __name__ == "__main__":
    # Example usage
    print("Catalan(0..10):", [catalan(i) for i in range(11)])
    print("Fibonacci(0..10):", [fibonacci(i) for i in range(11)])
    print("First ten primes:", first_ten_primes())
```

We will open the Terminal and run `python exercise1.py` to see what the functions output. I am lazy, so I will write `python exer` and then hit `Tab` to tab-complete the file name. The output was the following.

I don't remember how the Catalan numbers are computed, and I don't fully understand the Python code. I right-clicked in the [exercise1.py](./exercise1.py) file and scrolled down to `Explain`. A pop-up window provided me the option to have various lines of code explained. I can look up [Catalan numbers](https://en.wikipedia.org/wiki/Catalan_number) on Wikipedia to verify that some of the first Catalan numbers.

---
Third, the chatbot wrote a lot of code and it provided documentation for the functions. Suppose I wrote some code fast and did not document what the code does. I will copy the contents of [exercise1.py](./exercise1.py) into [exercise2.py](./exercise2.py) and deleted all the documentation. 

To document the code, we will tab-complete for AI suggestions and or explicitly invoke AI assistance with `Ctrl + I`. An example query could be:

```
Please write a docstring for this function that describes what the function does, gives type casting suggestions for the parameters, and creates some example function calls.
```
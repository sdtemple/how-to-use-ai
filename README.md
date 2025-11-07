# How to Use AI in Coding

This repository contributes to a tutorial on how (and how not to) use AI for coding assistance. We will provide some starter code which comprise of various exercises. Throughout the exercises, we will write and modify code that calculates certain fun number sequences, like the Catalan numbers. The tutorials are meant to be interactive when presented live!

Disclaimer: I am an experienced programmer, especially with Python. I am spot reading the AI-generated code to ensure that it makes sense, which is a best practice. I am role playing how to use Gen AI for beginner and intermediate programmers.

---

### Favorite hot-keys

- Click `Tab` to auto-complete some suggested code. You will see the suggested code pop up.
- Click `Esc` to reject the suggested code.
- Click `Ctrl + \`` to enter the Terminal window.
- Click `Ctrl + I` to ask for the chatbot in-line. This is where you could ask the AI for some specific code to be written.
- Click `Ctrl + Alt + I` to engage with the chatbot in a pop-up/side window. This is where you could have a conversation with the AI.
- `Ctrl + Shift + P` to select certain actions/tools in VS code
- `Ctrl + A` to grab everything in a file
- `Ctrl + X` to cut (move lines elsewhere) instead of copy
- `Windows + V` to see clipboard of previous copied text (Windows users) 

### Important buttons to click

- `+` in chatbot window to start a new conversation
- The clock in chatbot window to see prior conversations
- The clipboard to insert a file to work with an agent
- Toggle to change the AI (Claude, GPT, etc.)
- Toggle to use Agent versus Ask
- Choose the kernel in Jupyter notebooks (upper right).
    - Adjust the kernel to existing online kernels with GPUs and extra memory
- Click the chat icon at the top of the page instead of the hot-keys above


---

### Installation

These are instructions for first-time coders. If you already have VS code and a working package manager for Python (like Anaconda), you are all good.

1. Download VS Code (Virtual Studio Code) from the app store (if not already installed)
2. Download a package manager derivative of Anaconda () or Anaconda itself
    - [My instructions for mamba](https://isweep.readthedocs.io/en/latest/misc.html)
    - [Mamba the fast conda](https://github.com/mamba-org/mamba)
    - [The Anaconda enterprise](https://anaconda.org/)
3. Set up a conda environment in Terminal: `conda env create -f environment.yml`
4. Connect your VS Code to a GitHub account (especially Pro versions) for AI help
    - Sign up for an account at [github.com](https://www.github.com)
    - Students can get a free/discounted Pro version with an *edu email address [here](https://education.github.com/pack)
    - Connecting Copilot with VS code [here](https://code.visualstudio.com/docs/copilot/setup) 

---

## Start of tutorial

First, suppose I am inexperienced at writing Markdown (this .md file). We will build this README file with AI. The hot key `Ctrl + I` is your friend! You enter an environment where you can ask an AI chatboat to help you write code. I made the following query in the chatbot box.

```
Can you write a Markdown enumerated list with titles Exercise 1, Exercise 2, up to Exercises 5 and explicit links to python files titled exercise1.py, and up to exercise3.py?
```

1. Exercise 1 — [exercise1.py](./exercise1.py)
2. Exercise 2 — [exercise2.py](./exercise2.py)
3. Exercise 3 — [exercise3.py](./exercise3.py)

---

#### Exercise 1: writing some Python code

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

### Exercise 2: documenting some Python code

Third, the chatbot wrote a lot of code and it provided documentation for the functions. Suppose I wrote some code fast and did not document what the code does. I copied the contents of [exercise1.py](./exercise1.py) into [exercise2.py](./exercise2.py) and deleted all the documentation. 

To document the code, we will tab-complete for AI suggestions and/or explicitly invoke AI assistance with `Ctrl + I`. You can use `Ctrl + I` either where your mouse cursor is or highlight some text. An example query could be:

```
Please write a docstring for this function that describes what the function does, gives type casting suggestions for the parameters, and creates some example function calls.
```

---

### Exercise 3: rewriting some Python code

There are multiple ways to generate prime numbers. I copied the code in [exercise1.py](./exercise1.py) and deleted the Catalan number and Fibonacci sequence functions. 

To rewrite the code with different techniques to generate prime numbers, we will use `Ctrl + I` over highlighted text. The first instruction for the chatbot will be: 

```

I am an amateur number theorist, and I know that are multiple ways to generate prime numbers. I wrote a simple function to generate prime numbers, which is highlighted, but I would like to see an alternative implementation. Specifically, I would like you to write two functions that use the sieves of Eratosthenes and Atkin to generate prime numbers.
```

The second instruction will write code to check if the two different implementations provide the same prime number sequences.

```
Please write two functions that generate the first ten prime numbers with either the sieves of Atkin or Eratosthenes. Write the if __name__ == "__main__" code to verify that the two sieve implementations provide the same first ten prime numbers.
```

Finally, open the Terminal with `Ctrl + \`` and run `python exercise3.py` to verify that the prime number sequences match.

---

### Exercise 4: converting code to R and/or C

We can use generative AI coding assistance to translate between programming languages. Suppose we have a favorite programming language: Python. But, we are working with collaborators who want the project to use R code. We will use `Ctrl + I` over highlighted text. The instruction to the chatbot in the `exercise4.R` file will be:

```
I am an experienced Python programmer, and therefore implemented my code in Python. However, I have collaborators who prefer R. And, eventually, we will use some R packages in this project that are not available in Python. Please translate the following Python code into R code.
```

After the chatbot translates the code, we will verify it in Terminal. Click `Ctrl + \`` and then run `Rscript exercise4.R`. We will compare the result to our Python code. Run `python exercise3.py` in the Terminal.

Next, we will convert the Python code to C++ code. The instruction to the chatbot in the `exercise4.cpp` file will be:

```
I am an experienced Python programmer, and therefore implemented my code in Python. However, I have collaborators who prefer C++ because it can be faster or more memory efficient.Please translate the following Python code into C++ code.
```

After the chatbot translates the code, we will verify it in Terminal. Click `Ctrl + \`` and then run `g++ exercise4.cpp -o exercise4` to compile the program. Following compilation, run `./exercise4` and compare to the prior results. You will not be able to compile if you do not have a compiler like `g++`.

---

### Exercise 5: debugging code


We can use generative AI coding assistance to debug code. I wrote some code with bugs in [exercise5.py](./exercise5.py). First, we run `python exercise5.py` in the Terminal. We see that the 5th Catalan number is calculated as 50, whereas in [exercise1.py](./exercise1.py) and others we determined that the 5th Catalan number is 42. Additionally, we get a `TypeError` when we run our function to generate the Fibonacci sequence. 

1. Highlight the different code blocks and ask the chatbot to explain the error and fix it.
2. Run `python exercise5.py` on the saved file.
3. Confirm result by running our solved `python exercise1.py`.

---

### Exercise 6: plotting code

In my opinion, one of the best uses of AI can be writing code that plots data. In the IPython Notebook, we will follow steps to make plotting code with `Ctrl + I` and discuss how to further refine the plot in the Chat window.

---

### Exercise 7: how long should the responses be?

Here, in [exercise7.py](./exercise7.py), we will modify the length of the AI-written code by adjusting the number of tokens.


### Exercise 8: refactoring code

TBD


---

### Exercise: using an agent for data science

We are now data scientists about to analyze a new dataset. There are many columns in the dataset, and we don't know what those columns mean. I will download various datasets from Kaggle (a data science competitions website). To download, I need to have a user account and join the competitions ([smoker classification](https://www.kaggle.com/competitions/binary-prediction-of-smoker/data) and [home pricing](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)).

```
kaggle competitions download -c binary-prediction-of-smoker
```
```
kaggle competitions download -c house-prices-advanced-regression-techniques
```

You can unzip the files with the Terminal command `unzip binary-prediction-of-smoker.zip`. Next, open the chatbot agent window. Type `#file:train.csv`. We will have a conversation with the agent to better understand the dataset.


TBD

### Exercise: tricking the agent?

I made a tabular data file in `make-a-dataset.py` that I called `nonsensical-dataset.csv`. The columns concern values about fruits that could be healthy or not healthy for you. However, I generated this data from random distributions! Let's see what the chatbot thinks about the data.

Open the chatbot agent window (`Ctrl + Alt + I`), and type `#file:nonsensical-dataset.csv`.


TBD

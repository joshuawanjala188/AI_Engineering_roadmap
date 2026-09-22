"""
AI Engineering — Topic 7: Modules, Packages & Virtual Environments

Now we're moving from writing individual Python programs to building real Python projects.

As an AI engineer, you won't keep everything in one file like:

ai.py

A real project may contain:

AI Application
│
├── data
├── models
├── preprocessing
├── training
├── inference
├── API
├── configuration
├── tests
└── utilities

To manage this, you need to understand modules, packages, imports, dependencies, virtual environments, and project structure.

1. What Is a Module?

A Python module is simply a Python file.

For example:

math_utils.py

contains:

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b

That file is a module.

2. Importing a Module

Suppose you have:

project/
│
├── main.py
└── math_utils.py

Inside main.py:

import math_utils

Then:

result = math_utils.add(10, 5)

print(result)

Output:

15

The structure is:

main.py
   │
   │ import
   ↓
math_utils.py
   │
   ├── add()
   └── multiply()
3. Import Specific Functions

Instead of:

import math_utils

math_utils.add(10, 5)

you can do:

from math_utils import add

print(add(10, 5))

You can import multiple things:

from math_utils import add, multiply
4. Import Everything

You may see:

from math_utils import *

This imports everything from the module.

However, avoid this in professional code because it can make it unclear where names came from and can cause naming conflicts.

Prefer:

from math_utils import add

or:

import math_utils
5. Import Aliases

You can give an imported module a shorter name.

import math_utils as mu

Then:

print(mu.add(5, 3))

You'll see this constantly in data science:

import numpy as np
import pandas as pd

For example:

import numpy as np

values = np.array([1, 2, 3])
6. Python's Standard Library

Python comes with many modules.

Examples:

import math
import os
import sys
import json
import datetime
import random
import pathlib
import logging

You don't need to install these separately.

For example:

import math

print(math.sqrt(25))

Output:

5.0
7. Your Own Modules

Imagine you're building an AI application.

Instead of:

# main.py

def clean_data():
    ...


def normalize_data():
    ...


def train_model():
    ...


def predict():
    ...


def evaluate():
    ...

you can separate responsibilities:

ai_project/
│
├── main.py
│
├── preprocessing.py
│
├── training.py
│
└── evaluation.py

Then:

# preprocessing.py

def clean_data(data):
    ...


def normalize_data(data):
    ...

And:

# training.py

def train_model(data):
    ...

Then main.py can import them.

8. Why Modules Matter

Modules give you:

Organization

Related code stays together.

Reusability

You can reuse functions.

Maintainability

Smaller files are easier to understand.

Separation of responsibilities

For example:

data.py
→ data handling

model.py
→ model

training.py
→ training

evaluation.py
→ evaluation

This becomes essential as AI projects grow.

9. What Is a Package?

A package is a way of organizing multiple Python modules.

For example:

ai_project/
│
└── ml/
    ├── __init__.py
    ├── preprocessing.py
    ├── training.py
    └── evaluation.py

Here:

ml

is a package.

It contains:

preprocessing.py
training.py
evaluation.py
10. __init__.py

Historically, a regular Python package contains:

__init__.py

Example:

ml/
├── __init__.py
├── preprocessing.py
└── model.py

It tells Python and developers that this directory is intended to be a package.

Modern Python also supports namespace packages without __init__.py, but you'll still commonly see __init__.py in normal application packages.

11. Importing From a Package

Suppose:

project/
│
├── main.py
│
└── ml/
    ├── __init__.py
    ├── preprocessing.py
    └── model.py

You can write:

from ml.preprocessing import clean_data

Or:

from ml.model import Model

Then:

data = clean_data(data)

model = Model()
12. Subpackages

Large projects can have packages inside packages.

ai_project/
│
├── app/
│
├── data/
│   ├── loaders/
│   └── preprocessing/
│
├── models/
│   ├── classification/
│   └── regression/
│
└── training/

This allows you to organize large systems logically.

13. Absolute Imports

An absolute import starts from the project's package structure.

Example:

from ai_project.models.model import Model

Or within an application:

from app.models.model import Model

Absolute imports are generally easier to understand in larger projects.

14. Relative Imports

Suppose:

app/
├── models.py
└── training.py

Inside training.py:

from .models import Model

The . means:

Import from the current package.

Two dots:

from ..models import Model

means move up one package level.

Relative imports can be useful, but don't overcomplicate your project structure.

15. __name__

Remember this from the previous topic:

if __name__ == "__main__":
    main()

Every Python module has a special variable:

__name__

If you run:

python main.py

then:

__name__

is:

__main__

But if another file imports it:

import main

then:

main.__name__

is:

main

This is why:

if __name__ == "__main__":

is useful.

16. Avoid Running Code During Import

Consider:

# model.py

print("Model loaded")

class Model:
    pass

If you do:

import model

Python executes the top-level code.

You'll see:

Model loaded

That's why it's good practice to keep executable application logic inside functions and use:

if __name__ == "__main__":

when appropriate.

17. Dependencies

Your project may need external packages.

For example:

numpy
pandas
scikit-learn
torch
fastapi

These aren't all part of Python's standard library.

You install external packages using pip.

Example:

pip install numpy
18. What Is pip?

pip is Python's package installer.

For example:

pip install pandas

Then:

import pandas as pd

You can install multiple packages:

pip install numpy pandas scikit-learn
19. Why Virtual Environments?

Suppose project A needs:

package X version 1

while project B needs:

package X version 2

Installing everything globally can cause conflicts.

A virtual environment creates an isolated Python environment for a project.

Think:

Computer
│
├── Project A
│   └── Environment A
│       ├── Python
│       └── Packages
│
└── Project B
    └── Environment B
        ├── Python
        └── Packages
20. Creating a Virtual Environment

On Linux:

python3 -m venv .venv

This creates:

.venv/

inside your project.

Typical structure:

ai_project/
│
├── .venv/
├── main.py
└── requirements.txt
21. Activating the Environment

On Linux/macOS:

source .venv/bin/activate

Your terminal will typically show something like:

(.venv) user@computer:~/ai_project$

Now:

python

and:

pip

refer to the environment's tools.

22. Deactivating

When finished:

deactivate

Your terminal returns to the normal environment.

23. Installing Packages Inside the Environment

Activate:

source .venv/bin/activate

Then:

pip install numpy pandas

These packages are installed into the environment rather than your normal system Python environment.

24. requirements.txt

A Python project needs a way to tell others which dependencies it needs.

A simple approach is:

requirements.txt

Example:

numpy
pandas
scikit-learn

Then someone can install them using:

pip install -r requirements.txt
25. Freeze Dependencies

You can generate a requirements file from your environment:

pip freeze > requirements.txt

Then you'll get versions such as:

numpy==...
pandas==...
scikit-learn==...

This helps reproduce the environment.

However, pip freeze can include every installed package, including indirect dependencies. For larger professional projects, dependency management with pyproject.toml and a suitable tool is often cleaner.

26. pyproject.toml

Modern Python projects commonly use:

pyproject.toml

Instead of relying only on requirements.txt.

For example:

[project]
name = "my-ai-project"
version = "0.1.0"
description = "AI engineering project"
requires-python = ">=3.11"

dependencies = [
    "numpy",
    "pandas",
    "scikit-learn"
]

This provides project metadata and dependency information in a standardized format.

27. Why pyproject.toml Matters

It can describe:

Project name
Version
Python requirement
Dependencies
Build configuration
Tool configuration

Modern Python tooling increasingly centers around pyproject.toml.

28. Package Managers and Project Tools

You will eventually encounter tools such as:

pip
uv
Poetry
Pipenv
Conda

They solve overlapping but not identical problems.

For now, learn this workflow first:

python
   ↓
venv
   ↓
pip
   ↓
requirements.txt

Then later we'll learn modern dependency/project management in more depth.

29. Environment Variables

AI applications often need configuration that shouldn't be hard-coded.

For example:

API keys
Database URLs
Service configuration
Environment-specific settings

You shouldn't write:

API_KEY = "my-secret-key"

directly in your source code.

Instead, use environment variables.

30. Reading Environment Variables

Python provides os.environ and os.getenv().

import os

api_key = os.getenv("API_KEY")

Then your operating system can provide:

API_KEY=...

Your source code doesn't need to contain the secret itself.

31. .env Files

During development, you may use a .env file with a package such as python-dotenv.

Example:

.env

contains:

API_KEY=your-development-key
DATABASE_URL=...

Then:

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

Never commit real secrets to Git.

Add:

.env

to:

.gitignore
32. AI Project Structure

Let's create a realistic beginner AI project.

ai_project/
│
├── .venv/
│
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
│
├── src/
│   └── ai_project/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── data/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   └── preprocessing.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── model.py
│       │
│       ├── training/
│       │   ├── __init__.py
│       │   └── trainer.py
│       │
│       └── evaluation/
│           ├── __init__.py
│           └── metrics.py
│
└── tests/
    ├── test_data.py
    └── test_model.py

Don't worry if this looks complicated.

We'll build toward this gradually.

33. Data Module

loader.py:

def load_data():
    return [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

preprocessing.py:

def preprocess(data):
    return [
        [value / 10 for value in row]
        for row in data
    ]
34. Model Module

model.py:

class Model:

    def predict(self, data):
        return [
            sum(row)
            for row in data
        ]
35. Training Module

trainer.py:

def train(model, data):
    print("Training model...")
    return model
36. Evaluation Module

metrics.py:

def accuracy(actual, predicted):
    correct = 0

    for a, p in zip(actual, predicted):
        if a == p:
            correct += 1

    return correct / len(actual)

Now each module has a clear responsibility.

37. Connecting Everything

main.py might eventually look like:

from ai_project.data.loader import load_data
from ai_project.data.preprocessing import preprocess
from ai_project.models.model import Model
from ai_project.training.trainer import train


def main():

    data = load_data()

    data = preprocess(data)

    model = Model()

    model = train(model, data)

    predictions = model.predict(data)

    print(predictions)


if __name__ == "__main__":
    main()

Now we have:

main
 │
 ├── data.loader
 │
 ├── data.preprocessing
 │
 ├── models.model
 │
 └── training.trainer

This is the beginning of professional project architecture.

38. Circular Imports

One problem to watch out for is circular imports.

For example:

A imports B
B imports A

Like:

# a.py
from b import function_b

and:

# b.py
from a import function_a

This can cause import errors and confusing behavior.

The solution is usually to improve your architecture rather than trying to work around the circular dependency.

39. Single Responsibility

A good module should have a clear purpose.

Bad:

utils.py

containing:

database functions
ML models
API calls
data preprocessing
logging
authentication

Better:

database.py
models.py
api.py
preprocessing.py
logging_config.py

This principle is called separation of concerns.

40. AI Engineering Architecture

As your systems grow:

                 AI APPLICATION
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      Data           Models          API
        │              │              │
        ↓              ↓              ↓
 Preprocessing      Training       Services
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                  Evaluation
                       ↓
                  Monitoring

Modules and packages allow us to represent this architecture in code.

41. Practical Exercise

Create this project:

student_ai/
│
├── main.py
│
├── data.py
│
├── preprocessing.py
│
├── model.py
└── evaluation.py
data.py

Create:

def load_data():
    ...

Return:

[
    [10, 20],
    [30, 40],
    [50, 60]
]
preprocessing.py

Create:

def normalize(data):
    ...

Divide every value by 100.

model.py

Create:

class SimpleModel:
    ...

with:

predict(data)
evaluation.py

Create:

def mean_error(actual, predicted):
    ...
main.py

Import everything:

from data import load_data
from preprocessing import normalize
from model import SimpleModel
from evaluation import mean_error

Then build the pipeline:

load
 ↓
normalize
 ↓
model
 ↓
predict
 ↓
evaluate
42. Virtual Environment Exercise

Inside your project:

python3 -m venv .venv

Activate:

source .venv/bin/activate

Check:

python --version

Then:

pip --version

Install:

pip install numpy

Test:

python

Then:

import numpy as np

print(np.array([1, 2, 3]))

Exit Python:

exit()

Then deactivate:

deactivate
43. What You Should Understand

At this stage you should understand the relationship:

Python
  │
  ├── Module
  │     └── .py file
  │
  ├── Package
  │     └── collection of modules
  │
  ├── pip
  │     └── installs packages
  │
  ├── venv
  │     └── isolates environments
  │
  ├── requirements.txt
  │     └── dependency list
  │
  └── pyproject.toml
        └── modern project metadata/config

And the AI project:

                    AI PROJECT
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
         Data         Models         API
          │             │             │
          ↓             ↓             ↓
    Preprocessing    Training      Services
          │             │
          └─────────────┼─────────────┘
                        ↓
                   Evaluation
🎯 Mini-Project — AI Prediction Package

Build a small reusable package:

prediction_project/
│
├── .venv/
├── pyproject.toml
├── README.md
├── .gitignore
│
├── src/
│   └── prediction_project/
│       ├── __init__.py
│       ├── data.py
│       ├── preprocessing.py
│       ├── model.py
│       └── evaluation.py
│
└── tests/

Your package should:

Load data.
Validate data.
Preprocess data.
Make predictions.
Calculate an evaluation metric.
Use classes where appropriate.
Use type hints.
Use logging.
Use custom exceptions.
Use a virtual environment.
Store dependencies in project configuration.
Keep secrets out of the source code.

This project will combine Topics 1–7.

Next — Topic 8: NumPy & Numerical Computing

This is where we start entering the actual mathematical/programming foundation of AI.

We'll cover:

NumPy
  ↓
Arrays
  ↓
Dimensions
  ↓
Shape
  ↓
dtype
  ↓
Indexing
  ↓
Slicing
  ↓
Vectorization
  ↓
Broadcasting
  ↓
Matrix operations
  ↓
Linear algebra
  ↓
Random numbers
  ↓
Statistics
  ↓
Performance

Then we'll connect NumPy directly to the mathematics behind machine learning and neural networks.

next
Topic 8 — NumPy & Numerical Computing

NumPy is one of the most important Python libraries for AI, machine learning, data science, and scientific computing.

If Python gives you the programming language, NumPy gives you efficient mathematical computation.

1. What is NumPy?

NumPy = Numerical Python

Install it:

pip install numpy

Import it:

import numpy as np

The main object in NumPy is the array.

import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)

Output:

[10 20 30 40]
2. Why NumPy?

Python lists work:

numbers = [1, 2, 3, 4]

But AI systems often work with thousands, millions, or billions of numbers.

NumPy provides:

fast numerical operations
multidimensional arrays
vectorized calculations
matrix operations
linear algebra
random-number generation
statistical operations
efficient memory usage

For example:

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)

Output:

[11 22 33 44]

Instead of manually looping through every element.

3. Creating NumPy Arrays
From a list
import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x)
2D array
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x)

This represents:

1 2 3
4 5 6
3D array
x = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

AI frequently works with arrays having many dimensions.

For example, an image can be represented as:

height × width × channels

A batch of images might be:

batch × height × width × channels
4. Dimensions

NumPy tells us how many dimensions an array has.

x = np.array([1, 2, 3, 4])

print(x.ndim)

Output:

1

For a matrix:

x = np.array([
    [1, 2],
    [3, 4]
])

print(x.ndim)

Output:

2
5. Shape

shape tells you the size of every dimension.

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x.shape)

Output:

(2, 3)

Meaning:

2 rows
3 columns

This is extremely important in machine learning.

For example:

X.shape

might produce:

(1000, 20)

Meaning:

1000 samples
20 features
6. Size

size tells you the total number of elements.

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x.size)

Output:

6
7. Data Type

NumPy arrays have a data type.

x = np.array([1, 2, 3])

print(x.dtype)

You might get:

int64

For decimals:

x = np.array([1.5, 2.5, 3.5])

print(x.dtype)

You might get:

float64

You can specify the type:

x = np.array([1, 2, 3], dtype=np.float32)

print(x.dtype)

This matters greatly in AI because models often use types such as:

float32
float16
bfloat16

to reduce memory usage and speed up computation.

8. Special Arrays
zeros()
x = np.zeros(5)

print(x)
[0. 0. 0. 0. 0.]

2D:

x = np.zeros((3, 4))

Creates:

3 × 4

matrix of zeros.

ones()
x = np.ones(5)

print(x)

Output:

[1. 1. 1. 1. 1.]
full()
x = np.full((2, 3), 7)

print(x)

Output:

[[7 7 7]
 [7 7 7]]
9. arange()

Similar to Python's range():

x = np.arange(0, 10)

print(x)

Output:

[0 1 2 3 4 5 6 7 8 9]

You can specify a step:

x = np.arange(0, 10, 2)

print(x)

Output:

[0 2 4 6 8]
10. linspace()

linspace() creates evenly spaced numbers.

x = np.linspace(0, 1, 5)

print(x)

Output:

[0.   0.25 0.5  0.75 1.  ]

This is useful for:

mathematical functions
graphs
simulations
numerical analysis
11. Indexing

NumPy indexing starts at 0.

x = np.array([10, 20, 30, 40])

print(x[0])

Output:

10
print(x[2])

Output:

30
12. 2D Indexing
x = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

Get row 1, column 2:

print(x[0, 1])

Output:

20

Get:

50

using:

print(x[1, 1])
13. Slicing
x = np.array([10, 20, 30, 40, 50])

print(x[1:4])

Output:

[20 30 40]

You can also use:

x[:3]
[10 20 30]

And:

x[2:]
[30 40 50]
14. 2D Slicing
x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

Get the first two rows:

print(x[:2])

Get the first two columns:

print(x[:, :2])

Output:

[[1 2]
 [4 5]
 [7 8]]

The syntax:

x[rows, columns]

is extremely important.

15. Changing Values
x = np.array([10, 20, 30])

x[1] = 99

print(x)

Output:

[10 99 30]

For matrices:

x[0, 1] = 100
16. Mathematical Operations

This is where NumPy becomes extremely powerful.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

Addition:

print(a + b)
[5 7 9]

Subtraction:

print(a - b)
[-3 -3 -3]

Multiplication:

print(a * b)
[4 10 18]

Division:

print(a / b)
17. Scalar Operations

You can perform an operation on the entire array.

x = np.array([1, 2, 3, 4])

print(x * 10)

Output:

[10 20 30 40]

Or:

print(x + 5)
[6 7 8 9]

This is called vectorization.

18. Vectorization

Without NumPy:

numbers = [1, 2, 3, 4]

result = []

for n in numbers:
    result.append(n * 2)

With NumPy:

numbers = np.array([1, 2, 3, 4])

result = numbers * 2

Much cleaner.

And NumPy performs the underlying numerical operations efficiently.

This concept is fundamental to AI.

19. Aggregation Functions

Suppose:

scores = np.array([85, 45, 72, 91])

Mean:

print(np.mean(scores))

Minimum:

print(np.min(scores))

Maximum:

print(np.max(scores))

Sum:

print(np.sum(scores))

Standard deviation:

print(np.std(scores))

Variance:

print(np.var(scores))

These are heavily used in data analysis and ML.

20. Boolean Filtering

Suppose:

scores = np.array([85, 45, 72, 91, 38])

Find scores greater than 50:

print(scores > 50)

Output:

[ True False  True  True False]

You can use this to filter:

passed = scores[scores >= 50]

print(passed)

Output:

[85 72 91]

This is extremely useful for data preprocessing.

21. Broadcasting

Broadcasting allows NumPy to perform operations between arrays of compatible shapes.

Example:

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x + 10)

NumPy effectively applies 10 to every element:

[[11 12 13]
 [14 15 16]]

Another example:

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

y = np.array([10, 20, 30])

print(x + y)

Output:

[[11 22 33]
 [14 25 36]]

Broadcasting is extremely important in neural-network computations.

22. Reshaping

Suppose:

x = np.arange(12)

print(x)

You get:

[0 1 2 3 4 5 6 7 8 9 10 11]

Reshape it:

x = x.reshape(3, 4)

print(x)

Output:

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

This is critical when preparing data for ML models.

23. Flattening

Convert a multidimensional array into one dimension:

x = np.array([
    [1, 2],
    [3, 4]
])

flat = x.flatten()

print(flat)

Output:

[1 2 3 4]

You will frequently encounter this when preparing image data.

24. Transpose

Given:

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

Transpose:

print(x.T)

Output:

[[1 4]
 [2 5]
 [3 6]]

The shape changes:

(2, 3)

to:

(3, 2)
25. Matrix Multiplication

This is extremely important for AI.

Consider:

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

Matrix multiplication:

C = A @ B

print(C)

Output:

[[19 22]
 [43 50]]

You can also use:

np.matmul(A, B)
26. Dot Product

For vectors:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)

print(result)

Calculation:

1×4 + 2×5 + 3×6

=

32

The dot product is fundamental to:

linear regression
neural networks
embeddings
similarity
attention mechanisms
computer graphics
physics
27. Random Numbers

NumPy has a random-number system.

Modern NumPy code commonly uses:

rng = np.random.default_rng()

Generate random numbers:

numbers = rng.random(5)

print(numbers)

Generate integers:

numbers = rng.integers(1, 10, size=5)

print(numbers)

Example:

[3 8 1 6 4]

You can create a matrix:

weights = rng.random((3, 4))

print(weights)

This is conceptually similar to how ML models initialize parameters.

28. Random Seeds

For reproducible experiments:

rng = np.random.default_rng(42)

print(rng.random(5))

Using the same seed gives the same sequence.

This is useful when debugging machine-learning experiments.

29. Linear Algebra

NumPy includes many linear-algebra operations.

A = np.array([
    [1, 2],
    [3, 4]
])

Determinant:

print(np.linalg.det(A))

Inverse:

print(np.linalg.inv(A))

Eigenvalues:

values, vectors = np.linalg.eig(A)

Norm:

x = np.array([3, 4])

print(np.linalg.norm(x))

Output:

5.0

This connects directly to the linear algebra you have been studying.

30. NumPy and Machine Learning

Consider a simple linear model:

$$ y = Xw + b $$

In NumPy:

X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

w = np.array([0.5, 1.0])

b = 2

y = X @ w + b

print(y)

The important part is:

X @ w

That's matrix multiplication.

This basic operation appears everywhere in neural networks.

31. A Tiny Neural Network Calculation

Imagine:

x = np.array([2, 3])

weights = np.array([
    [0.5, 0.2],
    [0.1, 0.7]
])

bias = np.array([0.1, 0.2])

Compute:

z = x @ weights + bias

print(z)

Then apply an activation function.

For example, ReLU:

z = np.maximum(0, z)

print(z)

You've just implemented part of a neural-network layer using NumPy.

32. NumPy + Images

An image can be represented as an array.

For example:

Height = 224
Width = 224
Channels = 3

Its shape can be:

image.shape
(224, 224, 3)

The three channels are usually:

Red
Green
Blue

A batch of 32 images might have:

(32, 224, 224, 3)

This is why understanding NumPy shapes is so important for AI engineering.

33. NumPy + Data Engineering

Suppose you have:

scores = np.array([85, 45, 72, 91])

Calculate statistics:

print("Mean:", np.mean(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))
print("Standard deviation:", np.std(scores))

This becomes useful when preprocessing large datasets before sending them into ML models.

34. Important NumPy Skills to Master

You should become comfortable with:

np.array()
np.zeros()
np.ones()
np.arange()
np.linspace()

Array properties:

.ndim
.shape
.size
.dtype

Indexing:

x[i]
x[i, j]
x[start:end]

Operations:

+
-
*
/
**

Aggregation:

np.mean()
np.sum()
np.min()
np.max()
np.std()
np.var()

Array manipulation:

reshape()
flatten()
transpose()

Linear algebra:

@
np.dot()
np.linalg.norm()
np.linalg.inv()
np.linalg.det()
np.linalg.eig()

And especially:

vectorization
broadcasting
35. Practical Exercise

Create:

import numpy as np

scores = np.array([85, 45, 72, 91, 38, 67, 54, 88])

Your program should:

Exercise 1

Print:

Number of students
Average score
Highest score
Lowest score
Exercise 2

Find students who passed:

score >= 50
Exercise 3

Add 5 bonus points to every score.

Exercise 4

Calculate the standard deviation.

Exercise 5

Create a 2D array:

1 2 3
4 5 6
7 8 9

Then:

print its shape
print its dimensions
print its transpose
calculate its sum
calculate its mean
36. AI Engineering Mini-Project

Build a simple NumPy-based prediction system.

Suppose we have:

hours = np.array([1, 2, 3, 4, 5])

And:

scores = np.array([50, 55, 65, 70, 80])

Create a simple linear model:

weight = 6
bias = 45

predictions = hours * weight + bias

print(predictions)

Then calculate the errors:

errors = scores - predictions

print(errors)

Calculate Mean Absolute Error:

mae = np.mean(np.abs(errors))

print("MAE:", mae)

You've now connected:

Python
   ↓
NumPy
   ↓
Vectors
   ↓
Mathematics
   ↓
Prediction
   ↓
Evaluation
   ↓
Machine Learning
Your AI Engineering Progress

You have now covered the important Python foundation:

1. Python Fundamentals
        ↓
2. Functions
        ↓
3. Data Structures
        ↓
4. OOP
        ↓
5. Advanced Python
        ↓
6. Error Handling & Logging
        ↓
7. Modules, Packages & Environments
        ↓
8. NumPy & Numerical Computing  ← YOU ARE HERE
Next: Topic 9 — Pandas & Data Manipulation

We'll cover:

DataFrames
Series
Reading CSV/Excel/JSON
Selecting data
Filtering
Sorting
Missing values
Cleaning data
GroupBy
Aggregation
Merging
Joining
Pivot tables
Time series
Feature preparation
NumPy ↔ Pandas
Pandas ↔ ML

Then we'll start moving from Python programming into real AI/data workflows.

Tuesday 6:05 AM
next
Topic 9 — Pandas & Data Manipulation

Now we move from numerical computation with NumPy to working with real-world datasets.

If NumPy is mainly about numerical arrays, Pandas is about organizing, cleaning, exploring, and transforming data.

This is a major skill for:

Data Engineering
Data Science
Machine Learning
AI Engineering
Analytics
1. What is Pandas?

Pandas is a Python library for working with structured data.

Install it:

pip install pandas

Import it:

import pandas as pd

The two most important Pandas structures are:

Series
DataFrame
2. Series

A Series is basically a one-dimensional labeled collection of data.

import pandas as pd

scores = pd.Series([85, 45, 72, 91])

print(scores)

Output:

0    85
1    45
2    72
3    91
dtype: int64

Notice the index:

0
1
2
3

You can access an element:

print(scores[0])

Output:

85
3. DataFrame

A DataFrame is like a table.

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 45, 72, 91],
    "country": ["Kenya", "Uganda", "Kenya", "Tanzania"]
}

df = pd.DataFrame(data)

print(df)

Output:

      name  score  country
0    Alice     85    Kenya
1      Bob     45   Uganda
2  Charlie     72    Kenya
3    David     91 Tanzania

Think of it as:

             DataFrame
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
      name      score      country
       │          │           │
     Series     Series      Series

A DataFrame is one of the most important objects you'll encounter in data/AI work.

4. Inspecting Your Data

After loading a dataset, don't immediately start processing it.

First inspect it.

head()
print(df.head())

Shows the first rows.

You can specify how many:

print(df.head(2))
tail()
print(df.tail())

Shows the last rows.

shape
print(df.shape)

Example:

(4, 3)

Meaning:

4 rows
3 columns
columns
print(df.columns)
dtypes
print(df.dtypes)

This tells you the data type of each column.

5. info()

One of the most useful commands:

df.info()

It gives information such as:

number of rows
column names
missing values
data types
memory usage

When working with an unfamiliar dataset, this should be one of your first commands.

6. Statistical Summary

Use:

print(df.describe())

For numerical columns, you may see:

count
mean
std
min
25%
50%
75%
max

For example:

print(df["score"].describe())
7. Selecting a Column

Select one column:

print(df["name"])

Or:

print(df["score"])

You can also use:

print(df.score)

but the bracket form is generally safer and more flexible:

df["score"]
8. Selecting Multiple Columns
result = df[["name", "score"]]

print(result)

Output:

      name  score
0    Alice     85
1      Bob     45
2  Charlie     72
3    David     91
9. Selecting Rows with iloc

iloc uses integer positions.

print(df.iloc[0])

Gets the first row.

Get the first two rows:

print(df.iloc[:2])

Get row 2:

print(df.iloc[2])
10. Selecting with loc

loc works with labels/conditions.

For example:

print(df.loc[0])

You can select specific columns:

print(df.loc[:, ["name", "score"]])

The basic idea:

iloc → position
loc  → label/condition
11. Filtering Data

Suppose we want students who passed.

passed = df[df["score"] >= 50]

print(passed)

Output:

      name  score  country
0    Alice     85    Kenya
2  Charlie     72    Kenya
3    David     91 Tanzania

This is one of the most important Pandas operations.

12. Multiple Conditions

Students who scored at least 50 and are from Kenya:

result = df[
    (df["score"] >= 50) &
    (df["country"] == "Kenya")
]

print(result)

Use:

& → AND
| → OR
~ → NOT

Don't use Python's and / or for Pandas Series conditions.

13. Sorting

Sort by score:

sorted_df = df.sort_values("score")

print(sorted_df)

Descending:

sorted_df = df.sort_values("score", ascending=False)

Now the highest-scoring student appears first.

14. Adding a Column

Suppose we want to classify students:

df["passed"] = df["score"] >= 50

print(df)

You'll get:

      name  score  country  passed
0    Alice     85    Kenya    True
1      Bob     45   Uganda   False
2  Charlie     72    Kenya    True
3    David     91 Tanzania    True

This is an example of feature creation.

Feature engineering becomes very important later in machine learning.

15. Creating a Column from Calculations
df["bonus_score"] = df["score"] + 5

Or:

df["score_percentage"] = df["score"] / 100
16. Renaming Columns

Suppose:

df.columns

returns:

name
score
country

You can rename them:

df = df.rename(columns={
    "name": "student_name",
    "score": "exam_score"
})
17. Removing Columns
df = df.drop(columns=["country"])

Be careful: drop() returns a modified DataFrame unless you assign the result.

df = df.drop(columns=["country"])
18. Missing Data

Real-world datasets are rarely perfect.

You might have:

name     score
Alice    85
Bob      NaN
Charlie  72
David    91

NaN means the value is missing.

Check for missing values:

print(df.isna())

Count them:

print(df.isna().sum())
19. Removing Missing Rows
df = df.dropna()

This removes rows containing missing values.

But don't automatically do this with every dataset.

You need to understand why the values are missing first.

20. Filling Missing Values

You can replace missing values:

df["score"] = df["score"].fillna(0)

Or use the mean:

df["score"] = df["score"].fillna(
    df["score"].mean()
)

The correct approach depends on the dataset and problem.

21. Duplicate Data

Find duplicate rows:

print(df.duplicated())

Remove duplicates:

df = df.drop_duplicates()

Duplicate data can cause problems in analysis and ML training.

22. Unique Values

Find unique countries:

print(df["country"].unique())

Count unique countries:

print(df["country"].nunique())

Count how frequently each country appears:

print(df["country"].value_counts())

This is extremely useful when exploring categorical data.

23. GroupBy

This is one of the most powerful Pandas features.

Suppose:

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "score": [85, 45, 72, 91, 67],
    "country": ["Kenya", "Uganda", "Kenya", "Tanzania", "Kenya"]
}

df = pd.DataFrame(data)

Calculate average score by country:

result = df.groupby("country")["score"].mean()

print(result)

You might get:

country
Kenya       74.67
Tanzania    91.00
Uganda      45.00

This is extremely common in data analysis.

24. Multiple Aggregations
result = df.groupby("country")["score"].agg(
    ["mean", "min", "max", "count"]
)

print(result)

You can calculate several statistics at once.

25. Reading CSV Files

Most data projects involve files.

Suppose you have:

students.csv

Read it:

df = pd.read_csv("students.csv")

Then:

print(df.head())

This is one of the most common lines in data science.

26. Saving CSV
df.to_csv("clean_students.csv", index=False)

index=False prevents Pandas from adding the DataFrame index as an extra column.

27. Reading Excel

Install the necessary Excel engine if needed:

pip install openpyxl

Then:

df = pd.read_excel("students.xlsx")

Save:

df.to_excel("output.xlsx", index=False)
28. Reading JSON
df = pd.read_json("students.json")

JSON is especially important when working with:

APIs
web applications
backend systems
data pipelines
29. Pandas and APIs

Suppose an API returns JSON data.

Conceptually:

import requests
import pandas as pd

response = requests.get("https://example.com/api/data")

data = response.json()

df = pd.DataFrame(data)

print(df.head())

This is a common data-engineering workflow:

API
 ↓
JSON
 ↓
Python
 ↓
Pandas DataFrame
 ↓
Clean
 ↓
Transform
 ↓
ML/Data Warehouse
30. Merging DataFrames

Suppose we have:

students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

And:

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "score": [85, 45, 72]
})

Merge them:

result = pd.merge(
    students,
    scores,
    on="student_id"
)

print(result)

Output:

   student_id     name  score
0           1    Alice     85
1           2      Bob     45
2           3  Charlie     72

This is similar to a SQL JOIN.

31. Types of Joins

You'll encounter:

inner
left
right
outer

For example:

pd.merge(
    students,
    scores,
    on="student_id",
    how="left"
)

This becomes very important when working with databases and data warehouses.

32. Concatenating DataFrames

Suppose you have:

df1 = pd.DataFrame({
    "name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "name": ["Charlie", "David"]
})

Combine them:

result = pd.concat([df1, df2])
33. Applying Functions

You can apply a function to a column.

def classify(score):
    if score >= 50:
        return "Pass"
    return "Fail"

Then:

df["result"] = df["score"].apply(classify)

Now:

score    result
85       Pass
45       Fail
72       Pass
91       Pass
34. Vectorized Operations vs apply()

When possible, prefer Pandas/NumPy vectorized operations.

Instead of:

df["score"].apply(lambda x: x + 5)

you can simply use:

df["score"] + 5

Vectorized operations are usually cleaner and more efficient.

35. Data Cleaning Pipeline

A typical real-world workflow might look like:

import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.info())

df = df.drop_duplicates()

df["score"] = df["score"].fillna(
    df["score"].mean()
)

df["passed"] = df["score"] >= 50

df = df.sort_values(
    "score",
    ascending=False
)

df.to_csv(
    "clean_students.csv",
    index=False
)

Notice the pipeline:

Read
 ↓
Inspect
 ↓
Clean
 ↓
Transform
 ↓
Create features
 ↓
Sort/analyze
 ↓
Save

This pattern is extremely important.

36. Pandas + NumPy

They work together.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "score": [45, 67, 82, 91]
})

df["normalized"] = (
    df["score"] - np.mean(df["score"])
) / np.std(df["score"])

So you should think:

NumPy
 ↓
Numerical computation

Pandas
 ↓
Structured/tabular data

Together:

Pandas + NumPy
       ↓
Data preparation
       ↓
Machine Learning
37. Pandas → Machine Learning

Imagine a dataset:

age | income | experience | purchased
---------------------------------------
22  | 30000  | 1          | 0
30  | 50000  | 5          | 1
35  | 70000  | 8          | 1

Pandas can help you prepare:

X = df[
    ["age", "income", "experience"]
]

y = df["purchased"]

Now:

X
 ↓
Features

y
 ↓
Target

These can eventually be passed into a machine-learning model.

38. Important Concept: Features vs Target

Suppose:

df = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5],
    "attendance": [60, 70, 75, 85, 95],
    "exam_score": [45, 55, 65, 78, 90]
})

If we're predicting exam score:

X = df[["hours_studied", "attendance"]]

y = df["exam_score"]

Therefore:

X = input/features
y = target/output

This distinction is fundamental to machine learning.

39. Your Practical Exercise

Create this dataset:

import pandas as pd

data = {
    "name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank"
    ],
    "score": [85, 45, 72, 91, 67, 38],
    "country": [
        "Kenya",
        "Uganda",
        "Kenya",
        "Tanzania",
        "Kenya",
        "Uganda"
    ]
}

df = pd.DataFrame(data)

Now perform these tasks.

Exercise 1

Display:

df.head()
Exercise 2

Find:

number of rows
number of columns
column names
data types
Exercise 3

Find students who passed.

Exercise 4

Find students with scores above 70.

Exercise 5

Sort students from highest to lowest score.

Exercise 6

Calculate the average score.

Exercise 7

Calculate the average score by country.

Exercise 8

Create:
"""
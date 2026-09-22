"""
Machine Learning Fundamentals 🤖

Now we're moving from data analysis and statistics into the core of machine learning.

You've already learned:

Python
   ↓
NumPy
   ↓
Pandas
   ↓
Visualization
   ↓
Statistics & Probability
   ↓
Machine Learning

The goal of this topic is to understand how machine learning actually works, before we start building models.

1. What Is Machine Learning?

Machine Learning (ML) is a branch of AI where computers learn patterns from data and use those patterns to make predictions or decisions.

Traditional programming:

Rules + Data
     ↓
  Program
     ↓
  Output

Machine learning:

Data + Answers
      ↓
   Learning
      ↓
    Model
      ↓
 Predictions
Traditional programming example

You explicitly write:

if score >= 50:
    result = "Pass"
else:
    result = "Fail"

The rules are written by you.

Machine learning

You give the computer many examples:

Hours    Score    Result
2        40       Fail
3        45       Fail
5        60       Pass
7        75       Pass
9        90       Pass

The algorithm learns a relationship between the inputs and the result.

2. AI vs ML vs Deep Learning

These terms are related but aren't identical.

Artificial Intelligence
│
├── Machine Learning
│   │
│   ├── Classical ML
│   │
│   └── Deep Learning
│       ├── Neural Networks
│       ├── CNNs
│       ├── RNNs
│       └── Transformers
│
└── Other AI approaches
Artificial Intelligence

The broad field of building systems that perform tasks associated with intelligent behavior.

Machine Learning

Systems learn patterns from data.

Deep Learning

Machine learning using neural networks with multiple layers.

3. Types of Machine Learning

There are three major categories you should know:

Machine Learning
│
├── Supervised Learning
├── Unsupervised Learning
└── Reinforcement Learning

Let's examine each.

4. Supervised Learning

In supervised learning, the training data contains inputs and known answers.

For example:

Hours    Score
2        40
4        55
6        70
8        85

We know the answer for each training example.

The model learns:

Hours → Score

Then we can give it:

7 hours

and ask it to predict:

≈ 78

The exact prediction depends on the trained model and data.

5. Features and Target

This terminology is extremely important.

Consider:

Hours    Age    Attendance    Score
8        20       90%          85
5        19       80%          65

The features are the inputs used by the model:

Hours
Age
Attendance

The target is what we want to predict:

Score

Usually:

X = features
y = target

Example:

X = df[["hours", "age", "attendance"]]

y = df["score"]
6. Regression

Regression is supervised learning where the target is generally a continuous numerical value.

Examples:

Predict house price
Predict temperature
Predict salary
Predict exam score
Predict electricity consumption

Example:

Input:
hours = 7

Output:
predicted score = 78.4

The output isn't restricted to categories.

7. Classification

Classification predicts a category/class.

Examples:

Email → Spam / Not Spam

Image → Cat / Dog

Transaction → Fraud / Not Fraud

Patient record → Class A / Class B

Example:

Input:
email features

Output:
Spam
8. Regression vs Classification
Problem	Type
Predict house price	Regression
Predict exam score	Regression
Predict temperature	Regression
Spam detection	Classification
Cat vs dog	Classification
Fraud vs legitimate	Classification

A simple rule:

Numerical quantity → often regression.

Category → classification.

9. Unsupervised Learning

In unsupervised learning, the data doesn't come with target labels.

Example:

Customer
Age
Income
Purchases

We don't tell the algorithm which customer belongs to which group.

The algorithm attempts to discover structure.

A common technique is:

Clustering

For example:

             Customer data

                ↓

       ┌─────────────────┐
       │ Clustering      │
       └────────┬────────┘
                ↓
       ┌──────┬──────┬──────┐
       │Group1│Group2│Group3│
       └──────┴──────┴──────┘
10. Example of Clustering

Imagine customers described by:

Age
Income
Spending

An algorithm might discover groups such as:

Group A → younger/high spending
Group B → older/low spending
Group C → moderate spending

You didn't explicitly provide those labels.

The algorithm discovered patterns in the data.

11. Reinforcement Learning

Reinforcement learning is different.

An agent interacts with an environment.

          Action
Agent ─────────────→ Environment
  ↑                       │
  │                       │
  └──── Reward/State ─────┘

The agent tries to learn actions that maximize long-term reward.

Examples include:

game-playing systems
robotics
control systems
sequential decision-making

We'll study reinforcement learning separately later.

12. The Machine Learning Workflow

This is one of the most important things to memorize:

1. Define problem
       ↓
2. Collect data
       ↓
3. Clean data
       ↓
4. Explore data
       ↓
5. Prepare features
       ↓
6. Split data
       ↓
7. Train model
       ↓
8. Validate/tune
       ↓
9. Test model
       ↓
10. Evaluate
       ↓
11. Deploy
       ↓
12. Monitor

Notice that training the model is only one part of machine learning.

13. Training Data

Training data is the data used by the algorithm to learn model parameters.

Example:

Training data

Hours    Score
2        40
3        45
4        52
5        60
6        68

The model uses these examples to learn a relationship.

14. Testing Data

We don't want to test a model only on the examples it already learned from.

Instead, we keep some data separate.

Dataset
│
├── Training data
└── Test data

The test data acts as unseen data for the final evaluation.

15. Train/Test Split

Suppose we have 1,000 examples.

A simplified split might be:

1,000 examples
│
├── 800 → Training
└── 200 → Testing

In Python, scikit-learn provides:

from sklearn.model_selection import train_test_split

Example:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Here:

80% → training
20% → testing
16. Why Split the Data?

Suppose you study the exact questions that will appear on an exam.

Then you get:

100%

That doesn't necessarily mean you understand the subject.

Similarly, a machine-learning model could perform extremely well on data it has already seen but poorly on new data.

We want to measure generalization.

Generalization means:

How well does the model perform on previously unseen data?

17. Training vs Testing

Think about:

Training:
"Learn from these examples."

Testing:
"Now show me examples you haven't trained on."

This helps us estimate how well the model generalizes.

18. Validation Data

For more serious ML projects, we often use three sets:

Dataset
│
├── Training
├── Validation
└── Test

For example:

70% Training
15% Validation
15% Test
Training

Used to learn model parameters.

Validation

Used during model development for things such as:

selecting models
tuning hyperparameters
comparing configurations
Test

Reserved for final evaluation.

19. Parameters vs Hyperparameters

This distinction is important.

Parameters

Values learned by the model from training data.

For a linear model:

$$ y = wx+b $$

w and b are learned parameters.

Hyperparameters

Settings chosen outside the model-learning process.

Examples:

learning rate
number of trees
tree depth
number of neighbors
batch size
number of training epochs

We'll study these in detail later.

20. Linear Regression

Let's build our first conceptual model.

Suppose:

Hours → Score

A simple linear model looks like:

$$ y = wx+b $$

Where:

x = input
y = prediction
w = weight
b = bias

Example:

x = hours studied
y = predicted score
21. Example

Suppose:

w = 8
b = 20

Then:

$$ y = 8x + 20 $$

If:

x = 5

Then:

$$ y = 8(5)+20 $$ $$ y = 60 $$

The model predicts:

60
22. What Does Training Do?

The model doesn't magically know:

w = 8
b = 20

It learns parameters from data.

Conceptually:

Training data
     ↓
Learning algorithm
     ↓
Find useful parameters
     ↓
Model

The goal is to find parameters that produce predictions close to the observed targets.

23. Prediction Error

Suppose:

Actual score = 70
Predicted score = 65

Error:

$$ 70-65=5 $$

Another example:

Actual = 50
Predicted = 60

Error:

$$ 50-60=-10 $$

The sign tells us the direction of the error.

24. Loss Function

A loss function measures how bad the model's predictions are.

One common loss for regression is Mean Squared Error (MSE):

$$ MSE = \frac{1}{n} \sum_{i=1}^{n}(y_i-\hat y_i)^2 $$

Where:

y  = actual value
ŷ  = predicted value
n  = number of examples

The model's training process tries to reduce the loss according to the chosen learning algorithm.

25. Mean Absolute Error

Another metric is:

$$ MAE = \frac{1}{n} \sum |y_i-\hat y_i| $$

Suppose:

Actual:      [50, 70, 90]
Prediction:  [55, 65, 85]

Errors in absolute value:

5, 5, 5

Therefore:

MAE = 5

We'll cover evaluation metrics in much greater detail later.

26. Overfitting

This is one of the most important problems in machine learning.

Overfitting happens when a model learns the training data too specifically, including patterns that don't generalize well.

Imagine:

Training performance → 99%
Testing performance  → 60%

That's a warning sign.

Conceptually:

Training data
     ↓
Model memorizes too much
     ↓
Poor generalization
     ↓
Poor unseen-data performance
27. Underfitting

Underfitting is almost the opposite.

The model is too simple or insufficiently trained to capture the important patterns.

For example:

Training performance → 60%
Testing performance  → 58%

The model may not have learned enough.

28. The Three Cases

Think of:

Underfitting
    ↓
Model too simple

Good fit
    ↓
Learns useful patterns

Overfitting
    ↓
Learns training-specific details

The goal is good generalization, not simply the highest training score.

29. Bias and Variance

These are important statistical ideas in ML.

High bias

The model makes overly simplistic assumptions.

Can lead to:

Underfitting
High variance

The model is highly sensitive to the particular training dataset.

Can lead to:

Overfitting

Conceptually:

High Bias              High Variance
    ↓                       ↓
Underfitting             Overfitting

We'll go much deeper into this later.

30. Scikit-learn

One of the most important Python libraries for classical machine learning is:

scikit-learn

Install:

pip install scikit-learn

Import example:

from sklearn.linear_model import LinearRegression
31. Your First ML Model

Let's create a very small regression example.

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([
    40,
    50,
    60,
    70,
    80
])

model = LinearRegression()

model.fit(X, y)

The model learns from:

X → y
32. Make a Prediction

Now:

prediction = model.predict([[6]])

print(prediction)

The model should produce a value close to:

90

because the training data follows approximately:

1 → 40
2 → 50
3 → 60
4 → 70
5 → 80
33. Inspect the Learned Parameters

You can see the learned weight:

print(model.coef_)

and bias:

print(model.intercept_)

For this simple dataset, they should be approximately:

weight ≈ 10
bias   ≈ 30

because:

$$ y = 10x + 30 $$
34. A Realistic ML Dataset

Instead of using one feature:

hours

we might have:

hours
attendance
previous_score
assignments_completed

and target:

final_score

Then:

X = df[
    [
        "hours",
        "attendance",
        "previous_score",
        "assignments_completed"
    ]
]

y = df["final_score"]

Now the model has multiple features.

35. The Core ML Vocabulary

You should become comfortable with these terms:

Term	Meaning
Dataset	Collection of data
Feature	Input variable
Target	Value to predict
Sample	One data example
Model	Learned mathematical representation
Training	Learning from data
Prediction	Model output
Parameter	Learned model value
Hyperparameter	Configuration chosen by us
Loss	Training error measure
Metric	Performance measurement
Generalization	Performance on unseen data
Overfitting	Poor generalization due to excessive training-specific fitting
Underfitting	Failure to capture important patterns
36. Complete ML Picture

You can now think about machine learning like this:

                    DATA
                      │
                      ↓
                 Features X
                      │
                      ↓
              ┌──────────────┐
              │    MODEL     │
              │              │
              │  learns      │
              │  patterns    │
              └──────┬───────┘
                     │
                     ↓
                Prediction ŷ
                     │
                     ↓
              Compare with y
                     │
                     ↓
                   Loss
                     │
                     ↓
              Improve model

This process is repeated during training according to the learning algorithm
"""
"""
21. Pandas + Matplotlib

Since you've already learned Pandas, you can visualize a DataFrame directly.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 45, 72, 91]
}

df = pd.DataFrame(data)

df.plot(
    x="name",
    y="score",
    kind="bar"
)

plt.show()

This is one reason Pandas and Matplotlib work so well together.

22. Seaborn

Another important visualization library is:

Seaborn

Install:

pip install seaborn

Import:

import seaborn as sns

Seaborn works especially well for statistical visualization and EDA.

23. Seaborn Scatter Plot
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(
    data=df,
    x="hours",
    y="score"
)

plt.show()

You can also separate groups using another column.

For example:

sns.scatterplot(
    data=df,
    x="hours",
    y="score",
    hue="country"
)

plt.show()

This lets you investigate the relationship between:

hours
   ↓
score

while distinguishing
   ↓
country
24. Heatmaps 🔥

Heatmaps are particularly useful in AI/data science.

Suppose we have:

          hours  score  age
hours      1     0.8   0.1
score     0.8     1    0.2
age       0.1    0.2    1

We can visualize it.

First calculate correlations:

correlation = df.corr(numeric_only=True)

Then:

sns.heatmap(
    correlation,
    annot=True
)

plt.show()

annot=True displays the numerical values inside the cells.

25. Correlation

Correlation measures how strongly two variables move together.

It ranges from approximately:

-1 → 0 → +1

Roughly:

+1   strong positive relationship
 0   little/no linear relationship
-1   strong negative relationship

Example:

hours studied ↑
score ↑

could produce a positive correlation.

But:

Correlation does not automatically mean causation.

This distinction is extremely important in AI and statistics.

26. Exploratory Data Analysis — EDA

You've now reached an important AI engineering concept:

EDA = Exploratory Data Analysis

EDA means examining your dataset before building your model.

A typical workflow is:

Load data
   ↓
Inspect data
   ↓
Clean data
   ↓
Understand distributions
   ↓
Visualize relationships
   ↓
Find outliers
   ↓
Investigate missing values
   ↓
Understand features
   ↓
Prepare ML dataset
27. Example EDA Workflow

Suppose:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

Start with:

print(df.head())

Then:

print(df.info())

Then:

print(df.describe())

Check missing values:

print(df.isna().sum())

Check distributions:

df.hist()

plt.show()

Check relationships:

sns.pairplot(df)

plt.show()

Check correlations:

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.show()

This gives you a much better understanding of the dataset before ML begins.

28. Visualization in a Real AI Pipeline

A simplified AI workflow looks like:

             DATA
               ↓
        ┌──────────────┐
        │    Pandas    │
        └──────┬───────┘
               ↓
             EDA
               ↓
        ┌──────────────┐
        │ Visualization│
        └──────┬───────┘
               ↓
          Data Cleaning
               ↓
        Feature Engineering
               ↓
        Machine Learning
               ↓
            Model
               ↓
         Evaluation

Visualization is therefore not just making pretty charts.

It is part of understanding and validating your data.

29. Important Charts to Remember
Chart	Main purpose
Line	Change/trends
Bar	Compare categories
Scatter	Relationship between variables
Histogram	Distribution
Box plot	Spread/outliers
Heatmap	Correlation/matrix patterns
Pie	Simple proportions
Pair plot	Relationships among many numerical variables

For AI engineering, pay particular attention to:

Scatter plots + histograms + box plots + heatmaps.
"""
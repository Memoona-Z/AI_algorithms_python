# Simple Linear Regression from Scratch in Python

This folder contains an implementation of the **Simple Linear Regression algorithm from scratch in Python**. The implementation does **not use any machine learning libraries such as scikit-learn**, and uses only basic Python libraries for data processing, mathematical computation, and visualization.

## Files

- `simple-linear-regression.py` - Python script implementing Simple Linear Regression
- `Salary_Data.csv` - Dataset containing the relationship between Years of Experience and Salary

## About the Code

The code performs simple linear regression by:

1. Reading the dataset from `Salary_Data.csv` using pandas.
2. Extracting independent variable (Years of Experience) and dependent variable (Salary).
3. Computing the mean of both variables.

4. Calculating the slope (m) using the formula:

   m = Σ(x - x̄)(y - ȳ) / Σ(x - x̄)²

5. Calculating the intercept (b) using:

   b = ȳ - m x̄

6. Computing predicted values using the linear equation:

   y_pred = mx + b

7. Calculating total squared error between actual and predicted values.

8. Visualizing the dataset using a scatter plot and plotting the best fit regression line using Plotly.

The final output shows the regression line that best fits the given dataset based on minimum squared error.
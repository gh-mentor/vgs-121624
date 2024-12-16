"""
This app uses Python 3.14, numpy, matplotlib and pandas to generate a set of data points and plot them on a graph.
"""

# Include the required libraries 
import numpy as np              # numpy is used for numerical calculations
import matplotlib.pyplot as plt # matplotlib is used for plotting the data
import pandas as pd             # pandas is used for data manipulation

"""
Create a function 'gendata' that generates a set of 'n' data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the range of x values to generate.
- 'n' is the number of data points to generate. The default value is 100.
- 'f' is a function that takes a single argument and returns a single value. The default function is a non-linear function of x with random noise: x -> x ^ 1.5  + np.random.normal(0, 100).
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated by applying the 'f' function to the 'x' values.
- The data frame is sorted by the 'x' values.
Error Handling:
- If 'x_range' is not a tuple of two integers, raise a ValueError.
Examples 
- gendata((0, 100)) generates 100 data points with x values between 0 and 100.
- gendata((0, 100), n=50) generates 50 data points with x values between 0 and 100.
"""

def gendata(x_range, n=100, f=lambda x: x ** 1.5 + np.random.normal(0, 100)):
    # Check if x_range is a tuple of two integers
    if not isinstance(x_range, tuple) or len(x_range) != 2 or not all(isinstance(x, int) for x in x_range):
        raise ValueError("x_range must be a tuple of two integers")
    
    # Generate random x values in the specified range
    x = np.random.randint(x_range[0], x_range[1], n)
    
    # Generate y values using the specified function f
    y = f(x)
    
    # Create a pandas data frame with the generated data
    data = pd.DataFrame({'x': x, 'y': y})
    
    # Sort the data frame by the x values
    data = data.sort_values('x')
    
    return data 

"""
Create a function 'plot_data' that plots the data points from the data frame.
Arguments:
- 'data' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None
Details:
- The data points are plotted as a scatter plot.
- The plot has a title 'Data Points', x-axis label 'x', and y-axis label 'f(x)'.
- The plot is displayed using plt.show().
Error Handling:
- If 'data' is not a pandas data frame with columns 'x' and 'y', raise a ValueError.
Examples:
- data = gendata((0, 100))
"""

def plot_data(data):
    # Check if data is a pandas data frame with columns 'x' and 'y'
    if not isinstance(data, pd.DataFrame) or 'x' not in data.columns or 'y' not in data.columns:
        raise ValueError("data must be a pandas data frame with columns 'x' and 'y'")
    
    # Plot the data points
    plt.scatter(data['x'], data['y'])
    plt.title('Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

"""
Create a 'main' function that generates data points and plots them.
Arguments:
- None
Returns:
- None
Details:
- Generate 100 data points with x values between 0 and 100 using the default function.
- Plot the data points using the 'plot_data' function.
Examples:
- main()
"""

def main():
    data = gendata((10, 100))
    plot_data(data)


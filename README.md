[README (8).md](https://github.com/user-attachments/files/31646407/README.8.md)
# NumPy & Pandas Analyzer

## Project Description

**NumPy & Pandas Analyzer** is a simple, menu-driven Python program built to practice and demonstrate common **NumPy** and **Pandas** operations. The program lets the user create 1D, 2D, and 3D arrays and then perform different mathematical, statistical, and data-handling operations on them through an easy-to-use text menu.

This project was created as a college/academic Python project to strengthen understanding of arrays, object-oriented programming, and data analysis basics.

## Technologies Used

* Python
* NumPy
* Pandas

## Main Features

### 1. Array Creation
* Create 1D arrays
* Create 2D arrays
* Create 3D arrays

### 2. Mathematical Operations
* Addition
* Subtraction
* Multiplication
* Division
* Matrix multiplication

### 3. Array Manipulation
* Combine arrays
* Split arrays

### 4. Search, Sort and Filter
* Search for a particular value
* Sort array values
* Filter values greater than a given value

### 5. Statistical Operations
* Sum
* Mean
* Median
* Standard deviation
* Variance
* Minimum and maximum
* Percentile

### 6. Slicing and Indexing
* Slice 2D arrays
* Access elements using indexing for 1D, 2D, and 3D arrays

### 7. Pandas Integration
* Convert NumPy array data into a Pandas DataFrame
* Display the DataFrame
* Display Pandas summary statistics (using `df.describe()`)

## Python Concepts Demonstrated

| Concept | Used For |
|---|---|
| Classes and objects | Organizing the whole program using the `DataAnalytics` class |
| Constructor (`__init__`) | Initializing the array when the object is created |
| Properties and setters | Getting and setting the array safely |
| Class method | Creating an array filled with zeros |
| Static method | Calculating correlation between two arrays |
| Functions | Breaking the program into reusable operations |
| Loops | Taking multiple array elements as input |
| Conditional statements | Handling menu choices |
| Exception handling | Catching invalid input and errors |
| User input | Taking array size, elements, and menu choices from the user |
| NumPy arrays | Storing and processing numerical data |
| Pandas DataFrame | Displaying and summarizing data |

## NumPy Concepts Demonstrated

* `np.array()`
* `reshape()`
* `np.dot()`
* `np.concatenate()`
* `np.vstack()`
* `np.array_split()`
* `np.argwhere()`
* `np.sort()`
* Boolean filtering
* `np.sum()`
* `np.mean()`
* `np.median()`
* `np.std()`
* `np.var()`
* `np.min()`
* `np.max()`
* `np.percentile()`
* `np.zeros()`
* `np.corrcoef()`

## Pandas Concepts Demonstrated

* Creating a DataFrame
* Converting NumPy array data into a DataFrame
* Using `df.describe()` for summary statistics

## Menu

```
===================================
       NUMPY & PANDAS ANALYZER
===================================
1. Create Array
2. Mathematical Operations
3. Combine / Split Array
4. Search / Sort / Filter
5. Statistics
6. Slicing and Indexing
7. Show Data using Pandas
8. Exit
```

## How to Run the Project

1. Install Python on your computer.
2. Install NumPy and Pandas using:
   ```
   pip install numpy pandas
   ```
3. Save the Python file.
4. Open Command Prompt/Terminal in the project folder.
5. Run the program:
   ```
   python "PR.8 NumPy Analyzer.py"
   ```

## Example Usage

**Step 1: Create a 2D array**

```
1. Create Array
2. Mathematical Operations
3. Combine / Split Array
4. Search / Sort / Filter
5. Statistics
6. Slicing and Indexing
7. Show Data using Pandas
8. Exit
Enter your choice: 1

1. 1D Array
2. 2D Array
3. 3D Array
Enter your choice: 2
Enter number of rows: 2
Enter number of columns: 3
Enter element: 20
Enter element: 30
Enter element: 40
Enter element: 50
Enter element: 60
Enter element: 70

2D Array:
[[20. 30. 40.]
 [50. 60. 70.]]
```

**Step 2: Perform an operation (Addition)**

```
Enter your choice: 2

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Matrix Multiplication
Enter your choice: 1
Enter element: 10
Enter element: 20
Enter element: 30
Enter element: 40
Enter element: 50
Enter element: 60

Original Array:
[[20. 30. 40.]
 [50. 60. 70.]]

Second Array:
[[10. 20. 30.]
 [40. 50. 60.]]

Addition:
[[ 30.  50.  70.]
 [ 90. 110. 130.]]
```

**Step 3: View statistics**

```
Enter your choice: 5

1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Minimum and Maximum
7. Percentile
Enter your choice: 3
Median: 45.0
```

**Step 4: Exit the program**

```
Enter your choice: 8

Thank you for using NumPy & Pandas Analyzer!
Goodbye!
```

## Error Handling

The program is designed to handle common errors gracefully, including:

* Invalid numeric input
* Index out of range
* Division by zero
* Incorrect array size
* Invalid matrix dimensions
* Trying to perform operations before creating an array

## Project Structure

```
NumPy-Pandas-Analyzer/
│
├── PR.8 NumPy Analyzer.py
└── README.md
```

## Learning Objectives

This project helped in understanding:

* NumPy arrays and their dimensions
* Array manipulation (combining and splitting)
* Basic mathematical operations on arrays
* Statistical functions in NumPy
* Indexing and slicing of arrays
* Pandas DataFrames and summary statistics
* Basic object-oriented programming concepts in Python

## Future Improvements

* Adding visualization using Matplotlib
* Adding more statistical functions
* Saving results to a CSV file
* Loading arrays from external files
* Adding more Pandas operations

## Author

Developed by: **Pankti Patel**

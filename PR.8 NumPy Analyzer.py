import numpy as np
import pandas as pd


class DataAnalytics:

    def __init__(self, data=None):
        if data is not None:
            self._array = np.array(data)
        else:
            self._array = None

    # Get array
    @property
    def array(self):
        return self._array

    # Set array
    @array.setter
    def array(self, value):
        self._array = np.array(value)

    # Check array
    def check_array(self):
        if self._array is None:
            print("Please create an array first.")
            return False
        return True

    # ---------------- ARRAY CREATION ----------------

    def create_1d(self, elements):
        self._array = np.array(elements)

        print("\n1D Array:")
        print(self._array)

    def create_2d(self, rows, cols, elements):

        if len(elements) != rows * cols:
            print("Wrong number of elements.")
            return

        self._array = np.array(elements).reshape(rows, cols)

        print("\n2D Array:")
        print(self._array)

    def create_3d(self, depth, rows, cols, elements):

        if len(elements) != depth * rows * cols:
            print("Wrong number of elements.")
            return

        self._array = np.array(elements).reshape(depth, rows, cols)

        print("\n3D Array:")
        print(self._array)

    # ---------------- SLICING ----------------

    def slice_array(self):

        if not self.check_array():
            return

        if self._array.ndim != 2:
            print("Slicing is available for 2D arrays.")
            return

        try:
            r1 = int(input("Enter starting row: "))
            r2 = int(input("Enter ending row: "))
            c1 = int(input("Enter starting column: "))
            c2 = int(input("Enter ending column: "))

            result = self._array[r1:r2, c1:c2]

            print("\nSliced Array:")
            print(result)

        except ValueError:
            print("Please enter numbers only.")

    # ---------------- INDEXING ----------------

    def index_array(self):

        if not self.check_array():
            return

        try:

            if self._array.ndim == 1:

                index = int(input("Enter index: "))
                print("Value:", self._array[index])

            elif self._array.ndim == 2:

                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))

                print("Value:", self._array[row, col])

            elif self._array.ndim == 3:

                depth = int(input("Enter depth index: "))
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))

                print("Value:", self._array[depth, row, col])

        except IndexError:
            print("Index is out of range.")

        except ValueError:
            print("Please enter numbers only.")

    # ---------------- MATHEMATICAL OPERATIONS ----------------

    def math_operation(self, choice, elements):

        if not self.check_array():
            return

        if len(elements) != self._array.size:
            print("Please enter the same number of elements.")
            return

        second = np.array(elements).reshape(self._array.shape)

        print("\nOriginal Array:")
        print(self._array)

        print("\nSecond Array:")
        print(second)

        if choice == "1":

            result = self._array + second

            print("\nAddition:")
            print(result)

        elif choice == "2":

            result = self._array - second

            print("\nSubtraction:")
            print(result)

        elif choice == "3":

            result = self._array * second

            print("\nMultiplication:")
            print(result)

        elif choice == "4":

            if np.any(second == 0):
                print("Cannot divide by zero.")
                return

            result = self._array / second

            print("\nDivision:")
            print(result)

    # ---------------- MATRIX MULTIPLICATION ----------------

    def matrix_multiplication(self, second):

        if not self.check_array():
            return

        if self._array.ndim != 2:
            print("Matrix multiplication needs a 2D array.")
            return

        try:

            result = np.dot(self._array, second)

            print("\nMatrix Multiplication:")
            print(result)

        except ValueError:
            print("Matrix sizes are not suitable for multiplication.")

    # ---------------- COMBINE ARRAYS ----------------

    def combine_array(self, elements):

        if not self.check_array():
            return

        if len(elements) != self._array.size:
            print("Please enter the same number of elements.")
            return

        second = np.array(elements).reshape(self._array.shape)

        print("\nFirst Array:")
        print(self._array)

        print("\nSecond Array:")
        print(second)

        if self._array.ndim == 1:

            result = np.concatenate((self._array, second))

        else:

            result = np.vstack((self._array, second))

        print("\nCombined Array:")
        print(result)

    # ---------------- SPLIT ARRAY ----------------

    def split_array(self, parts):

        if not self.check_array():
            return

        try:

            result = np.array_split(self._array, parts)

            print("\nSplit Arrays:")

            for i, part in enumerate(result, 1):

                print("Part", i)
                print(part)

        except ValueError:
            print("Please enter a valid number.")

    # ---------------- SEARCH ----------------

    def search(self, value):

        if not self.check_array():
            return

        positions = np.argwhere(self._array == value)

        if len(positions) > 0:

            print("\nValue found at:")
            print(positions)

        else:

            print("\nValue not found.")

    # ---------------- SORT ----------------

    def sort(self):

        if not self.check_array():
            return

        result = np.sort(self._array)

        print("\nSorted Array:")
        print(result)

    # ---------------- FILTER ----------------

    def filter_array(self, value):

        if not self.check_array():
            return

        result = self._array[self._array > value]

        print("\nValues greater than", value)
        print(result)

    # ---------------- STATISTICS ----------------

    def statistics(self, choice):

        if not self.check_array():
            return

        if choice == "1":

            print("Sum:", np.sum(self._array))

        elif choice == "2":

            print("Mean:", np.mean(self._array))

        elif choice == "3":

            print("Median:", np.median(self._array))

        elif choice == "4":

            print("Standard Deviation:", np.std(self._array))

        elif choice == "5":

            print("Variance:", np.var(self._array))

        elif choice == "6":

            print("Minimum:", np.min(self._array))
            print("Maximum:", np.max(self._array))

        elif choice == "7":

            try:

                value = float(input("Enter percentile (0-100): "))

                if 0 <= value <= 100:

                    result = np.percentile(self._array, value)

                    print("Percentile:", result)

                else:

                    print("Enter a value between 0 and 100.")

            except ValueError:

                print("Please enter a number.")

    # ---------------- PANDAS ----------------

    def show_dataframe(self):

        if not self.check_array():
            return

        # Convert NumPy array into one-dimensional data
        data = self._array.flatten()

        # Create Pandas DataFrame
        df = pd.DataFrame({
            "Values": data
        })

        print("\nData using Pandas:")
        print(df)

        print("\nPandas Summary:")
        print(df.describe())

    # ---------------- CLASS METHOD ----------------

    @classmethod
    def create_zeros(cls, shape):

        return cls(np.zeros(shape))

    # ---------------- STATIC METHOD ----------------

    @staticmethod
    def correlation(array1, array2):

        return np.corrcoef(array1, array2)[0, 1]


# ==================================================
# MAIN PROGRAM
# ==================================================

def main():

    analyzer = DataAnalytics()

    while True:

        print("\n===================================")
        print("       NUMPY & PANDAS ANALYZER")
        print("===================================")

        print("1. Create Array")
        print("2. Mathematical Operations")
        print("3. Combine / Split Array")
        print("4. Search / Sort / Filter")
        print("5. Statistics")
        print("6. Slicing and Indexing")
        print("7. Show Data using Pandas")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # ---------------- CREATE ARRAY ----------------

        if choice == "1":

            print("\n1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            option = input("Enter your choice: ")

            try:

                if option == "1":

                    n = int(input("Enter number of elements: "))

                    elements = []

                    for i in range(n):

                        value = float(input("Enter element: "))

                        elements.append(value)

                    analyzer.create_1d(elements)

                elif option == "2":

                    rows = int(input("Enter number of rows: "))
                    cols = int(input("Enter number of columns: "))

                    elements = []

                    for i in range(rows * cols):

                        value = float(input("Enter element: "))

                        elements.append(value)

                    analyzer.create_2d(rows, cols, elements)

                elif option == "3":

                    depth = int(input("Enter depth: "))
                    rows = int(input("Enter rows: "))
                    cols = int(input("Enter columns: "))

                    elements = []

                    for i in range(depth * rows * cols):

                        value = float(input("Enter element: "))

                        elements.append(value)

                    analyzer.create_3d(depth, rows, cols, elements)

                else:

                    print("Invalid choice.")

            except ValueError:

                print("Please enter numbers only.")

        # ---------------- MATHEMATICAL OPERATIONS ----------------

        elif choice == "2":

            if not analyzer.check_array():
                continue

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Matrix Multiplication")

            option = input("Enter your choice: ")

            if option in ["1", "2", "3", "4"]:

                elements = []

                try:

                    for i in range(analyzer.array.size):

                        value = float(input("Enter element: "))

                        elements.append(value)

                    analyzer.math_operation(option, elements)

                except ValueError:

                    print("Please enter numbers only.")

            elif option == "5":

                if analyzer.array.ndim != 2:

                    print("Matrix multiplication needs a 2D array.")

                    continue

                try:

                    rows = int(input("Enter rows of second matrix: "))
                    cols = int(input("Enter columns of second matrix: "))

                    elements = []

                    for i in range(rows * cols):

                        value = float(input("Enter element: "))

                        elements.append(value)

                    second = np.array(elements).reshape(rows, cols)

                    analyzer.matrix_multiplication(second)

                except ValueError:

                    print("Please enter valid numbers.")

        # ---------------- COMBINE / SPLIT ----------------

        elif choice == "3":

            if not analyzer.check_array():
                continue

            print("\n1. Combine Arrays")
            print("2. Split Array")

            option = input("Enter your choice: ")

            if option == "1":

                elements = []

                try:

                    for i in range(analyzer.array.size):

                        value = float(input("Enter element: "))

                        elements.append(value)

                    analyzer.combine_array(elements)

                except ValueError:

                    print("Please enter numbers only.")

            elif option == "2":

                try:

                    parts = int(input("Enter number of parts: "))

                    analyzer.split_array(parts)

                except ValueError:

                    print("Please enter a valid number.")

        # ---------------- SEARCH / SORT / FILTER ----------------

        elif choice == "4":

            if not analyzer.check_array():
                continue

            print("\n1. Search")
            print("2. Sort")
            print("3. Filter")

            option = input("Enter your choice: ")

            if option == "1":

                try:

                    value = float(input("Enter value to search: "))

                    analyzer.search(value)

                except ValueError:

                    print("Please enter a number.")

            elif option == "2":

                analyzer.sort()

            elif option == "3":

                try:

                    value = float(input("Enter value: "))

                    analyzer.filter_array(value)

                except ValueError:

                    print("Please enter a number.")

        # ---------------- STATISTICS ----------------

        elif choice == "5":

            if not analyzer.check_array():
                continue

            print("\n1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum and Maximum")
            print("7. Percentile")

            option = input("Enter your choice: ")

            analyzer.statistics(option)

        # ---------------- SLICING / INDEXING ----------------

        elif choice == "6":

            if not analyzer.check_array():
                continue

            print("\n1. Slicing")
            print("2. Indexing")

            option = input("Enter your choice: ")

            if option == "1":

                analyzer.slice_array()

            elif option == "2":

                analyzer.index_array()

        # ---------------- PANDAS ----------------

        elif choice == "7":

            analyzer.show_dataframe()

        # ---------------- EXIT ----------------

        elif choice == "8":

            print("\nThank you for using NumPy & Pandas Analyzer!")
            print("Goodbye!")

            break

        else:

            print("Invalid choice. Please try again.")


# Start program
if __name__ == "__main__":

    print("Welcome to NumPy & Pandas Analyzer!")
    print("===================================")

    main()
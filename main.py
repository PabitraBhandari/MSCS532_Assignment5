# MSCS532_Assignment5
# Name: Pabitra Bhandari
# Course: Algorithms and Data Structures
# Instructor: Dr. Vanessa Ruth Cooper 

'''
This Python script compares the performance of two Quicksort implementations: one using a deterministic pivot (middle element) and the other using a random pivot.

Quicksort Implementations:
1. deterministic_quicksort: Uses the middle element as the pivot.
2. random_pivot_quicksort: Uses a randomly chosen pivot.
Performance Measurement:
measure_time: Times the execution of a sorting function.
print_table_for_input_type: Prints the timing results in a table format.
Testing: The script tests both Quicksort versions on random, sorted, and reverse-sorted arrays of various sizes, comparing their execution times.
'''

import time
import random

# Quicksort with a deterministic pivot (middle element)
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

# Quicksort with a random pivot selection
def random_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return random_pivot_quicksort(left) + middle + random_pivot_quicksort(right)

# Function to measure execution time of a sorting algorithm
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Function to print tables in a clean format
def print_table_for_input_type(results, input_type_key1, input_type_key2, subtitle):
    headers = ["Array Size", input_type_key1, input_type_key2]
    
    # Convert the results to row format for tabular display
    table = []
    for i in range(len(results['Array Size'])):
        row = [
            results['Array Size'][i],
            f"{results[input_type_key1][i]:.6f} s",
            f"{results[input_type_key2][i]:.6f} s"
        ]
        table.append(row)

    # Print the subtitle and the table in clean format using tabulate-style layout
    print(f"\n{subtitle}\n")
    print("{:<12} {:<28} {:<28}".format(*headers))
    for row in table:
        print("{:<12} {:<28} {:<28}".format(*row))

# Displaying test examples for both Quicksort implementations
test_array = [5, 3, 8, 6, 2, 7, 4, 1]

print("Quicksort example:")
print(f"Before Quicksort: {test_array}")
sorted_array = deterministic_quicksort(test_array.copy())
print(f"After Quicksort: {sorted_array}\n")

print("Randomized Quicksort example:")
print(f"Before Randomized Quicksort: {test_array}")
random_sorted_array = random_pivot_quicksort(test_array.copy())
print(f"After Randomized Quicksort: {random_sorted_array}\n")

# Generating test arrays of different sizes and distributions
sizes = [1000, 5000, 10000, 50000, 100000]
random_arrays = [[random.randint(0, 100000) for _ in range(size)] for size in sizes]
sorted_arrays = [list(range(size)) for size in sizes]
reverse_sorted_arrays = [list(range(size, 0, -1)) for size in sizes]

# Measuring time for both Quicksort implementations
results = {
    'Array Size': sizes,
    'Random Input (Deterministic)': [measure_time(deterministic_quicksort, arr.copy()) for arr in random_arrays],
    'Random Input (Randomized)': [measure_time(random_pivot_quicksort, arr.copy()) for arr in random_arrays],
    'Sorted Input (Deterministic)': [measure_time(deterministic_quicksort, arr.copy()) for arr in sorted_arrays],
    'Sorted Input (Randomized)': [measure_time(random_pivot_quicksort, arr.copy()) for arr in sorted_arrays],
    'Reverse Sorted (Deterministic)': [measure_time(deterministic_quicksort, arr.copy()) for arr in reverse_sorted_arrays],
    'Reverse Sorted (Randomized)': [measure_time(random_pivot_quicksort, arr.copy()) for arr in reverse_sorted_arrays],
}

# Displaying results in multiple tables
print("\nPerformance Analysis of Quicksort and Randomized Quicksort :\n")
print_table_for_input_type(results, 'Random Input (Deterministic)', 'Random Input (Randomized)', "Random Array Comparison")
print_table_for_input_type(results, 'Sorted Input (Deterministic)', 'Sorted Input (Randomized)', "Sorted Array Comparison")
print_table_for_input_type(results, 'Reverse Sorted (Deterministic)', 'Reverse Sorted (Randomized)', "Reverse Array Comparison")

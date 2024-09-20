
## Assignment 5: Quicksort Implementation, Analysis, and Randomization
#### Name : Pabitra Bhandari
#### Course: Algorithms and Data Structures (MSCS532)
#### Instructor: Dr. Vanessa Cooper
#### Date : 09/22/2024

## Introduction

This project implements and analyzes the **Quicksort** algorithm in two versions:
1. **Deterministic Quicksort**: The pivot is chosen as the middle element of the array.
2. **Randomized Quicksort**: The pivot is chosen randomly to reduce the likelihood of encountering the worst-case scenario.

The code performs both implementations, measures the time complexity empirically, and compares their performance on different types of input arrays (random, sorted, reverse-sorted). It also includes theoretical analysis, based on the study of **Chapter 7** and **Chapter 8** from *Introduction to Algorithms* by Cormen et al. (2022).

### Files:
- **[main.py](./main.py)**: Contains python script of this assignment.
- **[analysis.md](./analysis.md)**: Contains detailed analysis of the implementation and comparison of Quicksort between two versions.
- **[README.md](./README.md)**: Contains instructrions on how to run the code and a summary of findings in this assignment.

### Instructions to run code:
#### Running on windows 
1. Open a terminal (command prompt).
2. Navigate to the folder containing the python script using:

   ```bash
   cd path/to/your/script
   ```

3. Run the python file using:

   ```bash
   python your_script_name.py
   ```

#### Running on MacOS (Linux)
1. Open a terminal
2. Navigate to the folder containing the python script using:

   ```bash
   cd path/to/your/script
   ```

3. Run the python file using:

    ```bash
   python3 your_script_name.py
   ```

## Observe the Output:

The script first runs a test of both the deterministic and randomized Quicksort implementations. It prints:
- The original unsorted array.
- The sorted result for both implementations.

After that, the performance analysis is displayed in three separate tables, comparing both versions of Quicksort for different input types:
- Random arrays.
- Sorted arrays.
- Reverse sorted arrays.

## Summary of Findings

### Deterministic Quicksort:
- Performs efficiently on random inputs but shows significant performance degradation on already sorted or reverse-sorted inputs.
- The worst-case time complexity is \( O(n^2) \) in cases of highly unbalanced partitions, especially for sorted inputs.

### Randomized Quicksort:
- Random pivot selection significantly reduces the chances of encountering the worst-case scenario.
- Even for sorted or reverse-sorted inputs, Randomized Quicksort maintains \( O(n \log n) \) performance on average.

### Empirical Results:
- For random inputs, both implementations show similar performance.
- For sorted and reverse-sorted inputs, Randomized Quicksort consistently outperforms the deterministic version.

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). The MIT Press.

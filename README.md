
## Performance Analysis

| Input Size          | Time Complexity | Space Complexity                      |
|---------------------|-----------------|---------------------------------------|
| Tree with `n` nodes | O(n)            | O(w), where `w` is the maximum width  |
| Large Tree          | Linear          | Linear                                |
| Skewed Tree         | Linear          | Constant                              |


## Space Complexity

| Algorithm                     | Time Complexity | Space Complexity |
|-------------------------------|-----------------|------------------|
| Height of a Binary Tree       | O(n)            | O(h)             |
| Tree Level Order Traversal    | O(n)            | O(w)             |
| Swap Nodes at a Specific Level| O(n)            | O(w)             |

## Notes:

**Balanced Tree: For a balanced tree:**

- h ≈ log n, and 𝑤 ≈ 𝑛 / 2

**Skewed Tree: For a skewed tree:**

- ℎ = 𝑛, and 𝑤 = 1

## Sorting Algorithms

| Algorithm         | Best Case   | Average Case | Worst Case  | Space Complexity |
|-------------------|-------------|--------------|-------------|------------------|
| Bubble Sort       | O(n)        | O(n²)        | O(n²)       | O(1)             |
| Selection Sort    | O(n²)       | O(n²)        | O(n²)       | O(1)             |
| Insertion Sort    | O(n)        | O(n²)        | O(n²)       | O(1)             |
| Merge Sort        | O(n log n)  | O(n log n)   | O(n log n)  | O(n)             |
| Quick Sort        | O(n log n)  | O(n log n)   | O(n²)       | O(log n)         |
| Heap Sort         | O(n log n)  | O(n log n)   | O(n log n)  | O(1)             |
| Counting Sort     | O(n + k)    | O(n + k)     | O(n + k)    | O(n + k)         |
| Radix Sort        | O(nk)       | O(nk)        | O(nk)       | O(n + k)         |
| Bucket Sort       | O(n + k)    | O(n + k)     | O(n²)       | O(n + k)         |
| Shell Sort        | O(n log n)  | O(n log² n)  | O(n²)       | O(1)             |


### 1. Bubble Sort

Description: Repeatedly swaps adjacent elements if they are in the wrong order.

Use Case: Rarely used in practice; mainly for educational purposes.

### 2. Selection Sort

Description: Repeatedly selects the minimum element from the unsorted part and places it in the sorted part.

Use Case: Simple but inefficient for large datasets.

### 3. Insertion Sort

Description: Builds the sorted array one element at a time by inserting elements into their correct position.

Use Case: Efficient for small datasets or nearly sorted arrays.

### 4. Merge Sort

Description: Divides the array into halves, recursively sorts them, and then merges the sorted halves.

Use Case: Used when stability and guaranteed O(n log n) performance are required.

### 5. Quick Sort

Description: Divides the array using a pivot, then recursively sorts the partitions.

Use Case: Preferred for general-purpose sorting due to its efficiency.

### 6. Heap Sort

Description: Converts the array into a max heap, then repeatedly extracts the maximum element.

Use Case: Efficient for in-place sorting when stability is not required.

### 7. Counting Sort

Description: Counts the occurrences of each element and uses this information to place elements in order.

Use Case: Suitable for sorting integers or data within a limited range.

### 8. Radix Sort

Description: Sorts elements digit by digit, starting from the least significant digit.

k: Number of digits in the largest number.

Use Case: Used for integers or strings when the range of digits is limited.

### 9. Bucket Sort

Description: Divides elements into buckets, sorts each bucket, and combines the sorted buckets.

Use Case: Suitable for uniformly distributed data.

### 10. Shell Sort

Description: A variation of insertion sort with better performance for large arrays.

Use Case: Efficient for moderately sized arrays.


## Search algorithm

| Algorithm           | Best Case   | Average Case   | Worst Case   | Space Complexity |
|---------------------|-------------|----------------|--------------|------------------|
| Linear Search       | O(1)        | O(n)           | O(n)         | O(1)             |
| Binary Search       | O(1)        | O(log n)       | O(log n)     | O(1)             |
| Jump Search         | O(1)        | O(√n)          | O(√n)        | O(1)             | 

### 1. Linear Search

Description: Iterates through each element to find the target value.

Use Case: Suitable for small datasets or unsorted arrays.

### 2. Binary Search

Description: Compares the target value with the middle element and eliminates half of the remaining elements.

Use Case: Efficient for sorted arrays or when the dataset can be divided in half.

### 3. Jump Search

Description: Jumps ahead by a fixed number of steps and then performs a linear search.

Use Case: Efficient for large datasets with uniformly distributed values.
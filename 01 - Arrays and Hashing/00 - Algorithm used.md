# Prefix and Suffix Product Method

## Explanation
The **Prefix and Suffix Product Method** is a technique used to solve array problems where you need to calculate results based on cumulative values from both the left and right directions of the array. A common example is the "Product of Array Except Self" problem, where you calculate the product of all elements in the array except the one at the current index, without using division.

## Use Cases
- Problems requiring cumulative calculations, like:
  - **Product of Array Except Self**.
  - **Trapping Rain Water Problem** (finding max values to the left and right).
  - **Prefix Sum or Range Queries**.

## Algorithm Steps
1. **Initialize two cumulative values**: `left_product` for left-to-right traversal and `right_product` for right-to-left traversal.
2. **Perform a prefix pass**:
   - Traverse the array from left to right, updating a result array with cumulative products of elements to the left of the current index.
3. **Perform a suffix pass**:
   - Traverse the array from right to left, updating the result array by multiplying with cumulative products of elements to the right of the current index.
4. **Return the result array**.

## Python Code Example
```python
def product_except_self(nums):
    """
    Compute the product of the array except for the current index without division.
    :param nums: List of integers.
    :return: List of products excluding self.
    """
    n = len(nums)
    result = [1] * n  # Initialize the result array with 1

    # Calculate left products for each index
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Calculate right products for each index and multiply with the result
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    output = product_except_self(nums)
    print(f"Product except self for {nums}: {output}")
```

## Example Execution
### Input:
```python
nums = [1, 2, 3, 4]
```
### Output:
```plaintext
Product except self for [1, 2, 3, 4]: [24, 12, 8, 6]
```

## Complexity Analysis
- **Time Complexity**: O(n)
  - Two passes over the array (prefix and suffix).
- **Space Complexity**: O(1) (excluding the output array).
  - The algorithm uses constant extra space.

## Applications
This method is widely applicable in scenarios where cumulative calculations from both directions of an array are needed. It is efficient and avoids unnecessary recomputations, making it suitable for large datasets.


# Bucket Sorting

## Explanation
**Bucket Sort** is a comparison-free sorting algorithm that distributes elements of an array into a number of buckets. Each bucket is sorted individually, either using another sorting algorithm (e.g., quicksort) or by recursively applying bucket sort. Finally, the elements from all the buckets are concatenated to produce the sorted array.

Bucket Sort is most effective when the input data is uniformly distributed across a known range.

## Use Cases
- Sorting floating-point numbers in a range (e.g., [0, 1)).
- Sorting when the input is uniformly distributed.
- Handling datasets where the maximum value is known and small compared to the dataset size.

## Algorithm Steps
1. **Create Buckets**:
   - Divide the range of input values into `n` buckets (where `n` is the number of elements in the array).
   - Place each element in the appropriate bucket based on its value.
2. **Sort Buckets**:
   - Sort each bucket using another sorting algorithm (e.g., insertion sort).
3. **Concatenate Buckets**:
   - Combine all sorted buckets to produce the final sorted array.

## Python Code Example
```python
def bucket_sort(array):
    """
    Perform bucket sort on the given array.
    :param array: List of numbers to be sorted.
    :return: Sorted list.
    """
    if len(array) == 0:
        return array

    # Step 1: Create buckets
    num_buckets = len(array)
    max_value = max(array)
    min_value = min(array)
    bucket_range = (max_value - min_value) / num_buckets  # Range of each bucket

    buckets = [[] for _ in range(num_buckets)]

    # Step 2: Distribute array elements into buckets
    for num in array:
        bucket_index = int((num - min_value) / bucket_range)
        if bucket_index == num_buckets:  # Handle the edge case for the maximum value
            bucket_index -= 1
        buckets[bucket_index].append(num)

    # Step 3: Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Example usage
if __name__ == "__main__":
    nums = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    sorted_nums = bucket_sort(nums)
    print(f"Sorted array: {sorted_nums}")
```

## Example Execution
### Input:
```python
nums = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
```
### Output:
```plaintext
Sorted array: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
```

## Complexity Analysis
- **Time Complexity**:
  - Best Case: O(n + k), where `n` is the number of elements and `k` is the number of buckets.
  - Worst Case: O(n²), when all elements are placed in a single bucket.
- **Space Complexity**: O(n + k), where `k` is the number of buckets.

## Applications
- Sorting floating-point numbers within a specific range.
- Used when the dataset is uniformly distributed.
- Useful in scenarios where the range of numbers is known beforehand.


# Heap Data Structure

A **heap** is a special tree-based data structure that satisfies the **heap property**. It can be classified into two types:
- **Max-Heap**: The value of each node is greater than or equal to the values of its children.
- **Min-Heap**: The value of each node is less than or equal to the values of its children.

## When to Use a Heap

A heap is primarily used in scenarios where you need to repeatedly access the largest or smallest element. The most common use cases are:
- **Priority Queue**: Elements are dequeued in priority order, typically used in algorithms like Dijkstra's shortest path.
- **Heap Sort**: A sorting algorithm that uses the heap data structure to efficiently sort elements.
- **Efficiently Finding the Maximum/Minimum Element**: In a max-heap, the maximum element is always at the root, and in a min-heap, the minimum element is at the root.
  
## Main Functions of a Heap

1. **Insert**: Add a new element to the heap while maintaining the heap property.
2. **Extract**: Remove the root element (the largest or smallest depending on heap type) and re-adjust the heap.
3. **Peek**: Return the root element (maximum or minimum) without removing it.
4. **Heapify**: Reorganize the elements in an array or list to satisfy the heap property.
5. **Build-Heap**: Efficiently converts an unsorted array into a heap in linear time.

### Time Complexities

| Operation          | Time Complexity |
|--------------------|-----------------|
| Insert            | O(log n)        |
| Extract (Root)    | O(log n)        |
| Peek (Root)       | O(1)            |
| Heapify           | O(n)            |
| Build-Heap        | O(n)            |

## Code Example

Here's an implementation of a Min-Heap in Python using the `heapq` library:

```python
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        return heapq.heappop(self.heap)

    def peek_min(self):
        return self.heap[0] if self.heap else None

    def build_heap(self, array):
        heapq.heapify(array)
        self.heap = array

# Example usage
min_heap = MinHeap()

# Insert elements
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(5)
min_heap.insert(2)

# Extract minimum element
print(min_heap.extract_min())  # Output: 1

# Peek at the minimum element
print(min_heap.peek_min())    # Output: 2

# Build a heap from an unsorted array
unsorted_array = [9, 7, 5, 3, 8, 4, 2, 6]
min_heap.build_heap(unsorted_array)
print(min_heap.heap)  # Output: [2, 3, 4, 6, 8, 5, 9, 7]

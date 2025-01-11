# Two Pointer Algorithm

The **Two Pointer Algorithm** is a popular technique used to solve problems that involve processing a collection of data (like an array or a string). The algorithm uses two pointers that traverse the data structure, often from different starting points, and move towards each other or in a specific direction.

## When to Use a Two Pointer Algorithm

The Two Pointer technique is commonly used in the following scenarios:
- **Finding Pairs**: In problems where you need to find pairs or combinations in an array that satisfy a certain condition (e.g., sum equals a target).
- **Sorted Arrays**: When the array is sorted or can be sorted, two pointers can be used to optimize searching.
- **Subarray Problems**: Problems like finding the longest subarray with certain properties can be solved using this technique.
- **Palindrome Checking**: In strings, two pointers can be used to check whether the string is a palindrome by comparing characters from both ends.

## Main Functions of Two Pointer Algorithm

1. **Initialization**: Two pointers are initialized at different positions (either at the beginning, end, or one at each end of the array).
2. **Pointer Movement**: The pointers are moved according to specific conditions, usually incrementing, decrementing, or moving based on certain conditions being met.
3. **Termination**: The algorithm terminates when a certain condition is met, like when the pointers meet or exceed a boundary.

### Time Complexity

| Operation             | Time Complexity |
|-----------------------|-----------------|
| Initializing Pointers | O(1)            |
| Pointer Movement      | O(n)            |
| Total Time Complexity | O(n)            |

## Code Example

Here’s an example of the Two Pointer Algorithm to find two elements in a sorted array that sum to a target value:

```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = two_sum(nums, target)
print(result)  # Output: [0, 8] (1 + 9 = 10)

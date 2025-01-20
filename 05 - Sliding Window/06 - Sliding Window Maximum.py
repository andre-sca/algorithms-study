from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    deq = deque()  # This will store indices of elements
    res = []
    
    for i in range(len(nums)):
        # Remove elements outside the current window
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove elements smaller than the current element from the deque
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        # Add current element's index to the deque
        deq.append(i)
        
        # If the window has reached size k, add the max (front of deque) to result
        if i >= k - 1:
            res.append(nums[deq[0]])  # Maximum is at the front of the deque

    return res
    



print(maxSlidingWindow([1,2,1,0,4,2,6], 3))
# Binary Search
<!-- Description of the challenge -->
Binary search in a sorted 1D array

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Binary Search Whiteboard](./binary_search.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I think I did a fairly standard approach. Set the left and right extremes, divide them by two, check value, and then set either extreme to mid +/- 1 if too low/high.  
Time complexity should be O(log n) and space complexity should be constant.

## Solution
<!-- Show how to run your code, and examples of it in action -->
```
def binary_search(arr, value):
    if not isinstance(arr, list):
        raise TypeError("No")
        
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == value:
            return mid
        
        elif arr[mid] < value:
            left = mid + 1
        
        else:
            right = mid - 1
            
    return -1
```
# Array Insert Shift
<!-- Description of the challenge -->
Insert and shift an array in middle at index.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![ShiftArray Whiteboard](./arrayinsertshift.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I calculated the length of the given array, divided by two rounding up, and then inserted the value at the index.
Time complexity should be O(n) while space should be constant. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

> def insert_shift_array(arr, n):  
> &nbsp;&nbsp;&nbsp;&nbsp;index = math.ceil(len(arr) / 2)  
> &nbsp;&nbsp;&nbsp;&nbsp;arr.insert(index, n)  
> &nbsp;&nbsp;&nbsp;&nbsp;# arr = arr[:index] + [n] + arr[index:]  ### Option b  
> &nbsp;&nbsp;&nbsp;&nbsp;return arr  
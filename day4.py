## 4.1 Write out the code for the earlier sum function
def sum_num(arr):
    if len(arr)==0:
        return 0
    print(arr[0])
    return arr[0]+sum_num(arr[1:])

arr=[1,2,3,4,5,6]
print(f"sum of the numbers is: {sum_num(arr)}")


## Write a recursive function to count the number of items in a list.
def count_items(arr):
    if len(arr)==0:
        return 0
    return 1+count_items(arr[1:])
arr=[1,2,3,4,5,6]
print(f"count of the numbers is: {count_items(arr)}")


## Write a recursive function to find the maximum number in a list.

def find_max(arr):
    if len(arr)==0:
        return 0
    return max(arr[0],find_max(arr[1:]))

arr=[1,2,3,44,5,6]
print(f"max of the numbers is: {find_max(arr)}")

## write a recursive function for the binary search

def binary_Search(arr, target, low, high):

    # Base case
    if low > high:
        return False

    mid = (low + high) // 2

    if arr[mid] == target:
        return True

    if arr[mid] > target:
        return binary_Search(arr, target, low, mid - 1)

    return binary_Search(arr, target, mid + 1, high)


arr = [1, 2, 3, 4, 5, 6]
target = 5

print(f"Is {target} present in the list: "
      f"{binary_Search(arr, target, 0, len(arr) - 1)}")
print(f"index of {target} in the list is: {arr.index(target)}")



## Reverse a string using recursion
def reverse_string(s):
    if len(s)==0:
        return s
    return s[-1]+reverse_string(s[:-1])

s="Hello"
print(f"Reverse of the string is: {reverse_string(s)}")


## Calculate x^n recursively

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

x=4
n=3
print(f"{x}^{n} is: {power(x,n)}")

### Calculate factorial
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    return n*fact(n-1)

n=5
print(f"Factorial of {n} is: {fact(n)}")


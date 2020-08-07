def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if target == arr[i]:
            return i
        else:
            pass
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0 
    high = len(arr)-1
    found = False
    # Your code here
    while not found and low <= high:
        guess = low + high // 2

        if target == arr[guess]:
            found = True
            return guess
        elif target > arr[guess]:
            low = guess + 1
        elif target < arr[guess]:
            high = guess - 1

    return -1   # not found
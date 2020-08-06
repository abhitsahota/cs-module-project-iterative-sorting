# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # starting at index 0

    # for each element in the array
    for el in range(0, len(arr)):
        # end if there were no swaps on this iteration, otherwise run it again
        swapped = 0
        for pos in range(0, len(arr)-1):
            if arr[pos] > arr[pos+1]:
                swapped +=1
                num = arr[pos]
                arr[pos] = arr[pos+1]
                arr[pos+1] = num
            else: 
                pass
        if swapped == 0:
            return arr
    return arr

print(bubble_sort([8,7,6,5,3,2,5,1,9,7]))
print(bubble_sort([1,2,3,4,5,6,7,8,9,10]))


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

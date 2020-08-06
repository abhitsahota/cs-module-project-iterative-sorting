### BigO Notation

#insertation sort
import random
my_range = 100
size = 15


list = random.sample(range(my_range), size)

print(list)

def insertion_sort(nums):
# first element is on the sort side
# starting on the second item, iterate until the end of the array

    for i in range(1, len(nums)):
    # the current number at the index is sorted, next value is the one to be sorted
        current_num = nums[i] # this is number we are sorting
        j = i # this is position value we are checking

        # move the number to be sorted through the array
        # move it until it greater than number before it and less than the one after it
        # or we reach the start of the array
        while j > 0 and current_num < nums[j-1]:
            # shift over the current value to left incrementally
            nums[j] = nums[j-1]
            j -= 1
        # set value at the current index to the current number
        # j represents the new location for the current number
        nums[j] = current_num

    return nums

print(insertion_sort([8,7,6,5,3,2,5,1,9]))
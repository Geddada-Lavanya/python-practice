# Linear Search (Simple Explanation)

# Linear search checks each element one by one until the target is found or the array ends.


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # target found at index i
    return -1           # target not found


# Example
arr = [10, 25, 30, 45, 60]
target = 30

index = linear_search(arr, target)
print(index)

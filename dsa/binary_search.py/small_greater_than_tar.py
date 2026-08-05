# 4. Find Smallest Letter Greater Than Target
# Problem Statement

# You are given a sorted list of letters and a target letter.
# Return the smallest letter strictly greater than the target.
# Letters wrap around.

# Example
# letters = ["c","f","j"], target = "j" → Output: "c"

def nextGreatestLetter(letters, target):
    left, right = 0, len(letters) - 1
    ans = letters[0]

    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            ans = letters[mid]
            right = mid - 1
        else:
            left = mid + 1

    return ans

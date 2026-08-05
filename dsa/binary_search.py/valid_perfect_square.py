# 5. Valid Perfect Square
# Problem Statement

# Given a positive integer num, check if it is a perfect square
# Do not use built-in sqrt.

# Example
# num = 16 → True
# num = 14 → False

def isPerfectSquare(num):
    left, right = 1, num

    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid

        if sq == num:
            return True
        elif sq < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

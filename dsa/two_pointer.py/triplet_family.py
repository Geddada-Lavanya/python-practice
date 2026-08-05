# Given an array arr of integers. First sort the array then find whether three numbers are such that the sum of two elements equals the third element.

# Example:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: true
# Explanation: The pair (1, 2) sums to 3.


class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n=len(arr)
        for k in range(n-1,1,-1):
            i=0
            j=k-1
            while i<j:
                if arr[i]+arr[j]==arr[k]:
                    return True
                elif arr[i]+arr[j]<arr[k]:
                    i+=1
                else:
                    j-=1
        return False
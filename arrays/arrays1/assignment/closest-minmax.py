# Problem Description

# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

# and at least one occurrence of the minimum value of the array.



# Problem Constraints

# 1 <= |A| <= 2000



# Input Format

# First and only argument is vector A



# Output Format

# Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array



# Example Input

# Input 1:

# A = [1, 3]

# Input 2:

# A = [2]



# Example Output

# Output 1:

#  2

# Output 2:

#  1



# Example Explanation

# Explanation 1:

#  Only choice is to take both elements.

# Explanation 2:

#  Take the whole array.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = -float('infinity')
        mn = float('infinity')

        N = len(A)
        for i in range(N):
            mx = max(mx, A[i])
            mn = min(mn, A[i])

        a = -1
        b = -1

        ans = N+1
        for i in range(N):
            if A[i] == mx:
                a = i
            if A[i] == mn:
                b = i

            if a >= 0 and b >= 0:
                ans = min(abs(a-b)+1,ans)

        return ans

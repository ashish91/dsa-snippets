# Problem Description

# Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



# Problem Constraints

# 1 <= |A| <= 100000



# Input Format

# First and only argument is the vector A



# Output Format

# Return one integer, the answer to the question



# Example Input

# Input 1:

# A = [0, 1, 0, 2]

# Input 2:

# A = [1, 2]



# Example Output

# Output 1:

# 1

# Output 2:

# 0



# Example Explanation

# Explanation 1:

# 1 unit is trapped on top of the 3rd element.

# Explanation 2:

# No water is trapped.

class Solution:
  # @param A : tuple of integers
  # @return an integer
  def trap(self, A):
        N = len(A)
        l = [0] * N
        r = [0]*N

        l[0] = A[0]
        r[N-1] = A[N-1]

        for i in range(1,N):
            l[i] = max(l[i-1],A[i])

        for i in range(N-2, -1,-1):
            r[i] = max(r[i+1],A[i])

        rain = 0
        for i in range(N):
            rain += min(l[i],r[i])-A[i]

        return rain

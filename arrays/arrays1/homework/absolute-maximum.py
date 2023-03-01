# Problem Description

# Given 4 array of integers A, B, C and D of same size, find and return the maximum value of | A [ i ] - A [ j ] | + | B [ i ] - B [ j ] | + | C [ i ] - C [ j ] | + | D [ i ] - D [ j ] | + | i - j| where i != j and |x| denotes the absolute value of x.



# Problem Constraints

# 2 <= length of the array A, B, C, D <= 100000
# -106 <= A[i] <= 106



# Input Format

# The arguments given are the integer arrays A, B, C, D.



# Output Format

# Return the maximum value of | A [ i ] - A [ j ] | + | B [ i ] - B [ j ] | + | C [ i ] - C [ j ] | + | D [ i ] - D [ j ] | + | i - j|



# Example Input

# Input 1:

#  A = [1, 2, 3, 4]
#  B = [-1, 4, 5, 6]
#  C = [-10, 5, 3, -8]
#  D = [-1, -9, -6, -10]

# Input 2:

#  A = [1, 2]
#  B = [3, 6]
#  C = [10, 11]
#  D = [1, 6]



# Example Output

# Output 1:

#  30

# Output 2:

#  11



# Example Explanation

# Explanation 1:

#  Maximum value occurs for i = 0 and j = 1.

# Explanation 2:

# There is only one possibility for i, j as there are only two elements in the array.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)
        
        ans = 0
        for k in range(16):
            mx = -float('infinity')
            mn = float('infinity')
            for i in range(N):
                curr = A[i]
                rest = [B[i],C[i],D[i],i]
                
                for j in range(4):
                    if k&(1<<j):
                        curr += rest[j]
                    else:
                        curr -= rest[j]
                
                mx = max(mx,curr)
                mn = min(mn,curr)
            ans = max(ans,mx-mn)
            
        return ans
                

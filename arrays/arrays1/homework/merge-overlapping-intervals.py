# Problem Description

# Given a collection of intervals, merge all overlapping intervals.



# Problem Constraints

# 1 <= Total number of intervals <= 100000.



# Input Format

# First argument is a list of intervals.



# Output Format

# Return the sorted list of intervals after merging all the overlapping intervals.



# Example Input

# Input 1:

# [1,3],[2,6],[8,10],[15,18]



# Example Output

# Output 1:

# [1,6],[8,10],[15,18]



# Example Explanation

# Explanation 1:

# Merge intervals [1,3] and [2,6] -> [1,6].
# so, the required answer after merging is [1,6],[8,10],[15,18].
# No more overlapping intervals present.

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, ints):
        N = len(ints)
        if N == 1:
            return ints

        ints.sort(key=lambda x:x.start)
        ans = [ints[0]]
        for i in range(1,N):
            curr = ans[-1]
            if (curr.end >= ints[i].start and curr.end <= ints[i].end) or (curr.start <= ints[i].start and ints[i].end <= curr.end):
                curr.start = min(ints[i].start,curr.start)
                curr.end = max(ints[i].end,curr.end)
            else:
                ans.append(ints[i])


        return ans

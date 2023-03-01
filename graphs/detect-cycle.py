import sys

sys.setrecursionlimit(1000000)
class Solution:
  # @param A : integer
  # @param B : list of list of integers
  # @return an integer
  def solve(self, A, B):
    graph = {}

    for i in range(1,A+1):
      graph[i] = []

    for edge in B:
      graph[edge[0]].append(edge[1])

    vis = [0]*(A+1)
    def dfs(node):
      nonlocal vis

      for nei in graph[node]:
        if vis[nei] == 0:
          vis[nei] = 1
          if dfs(nei) == 1:
            return 1
        elif vis[nei] == 1:
          return 1
        vis[nei] = 2

    for node in range(1,A+1):
      if vis[node] == 0:
        vis[node] = 1
        if dfs(node) == 1:
          return 1
        vis[node] = 2

    return 0



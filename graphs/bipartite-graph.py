class Solution:
  # @param A : integer
  # @param B : list of list of integers
  # @return an integer
  def solve(self, A, B):
    graph = dict()
    for i in range(A):
      graph[i] = []

    for edge in B:
      graph[edge[0]].append(edge[1])
      graph[edge[1]].append(edge[0])

    coloring = [-1]*A
    def bfs(node):
      nonlocal coloring
      q = [node]
      color = 0
      coloring[node] = color
      while len(q) > 0:
        color ^= 1
        nex = []

        for node in q:
          for nei in graph[node]:
            if coloring[nei] == -1:
              coloring[nei] = color
              nex.append(nei)
            elif color != coloring[nei]:
              return 0

        q = nex

    for node in range(A):
      if coloring[node] == -1:
        if bfs(node) == 0:
          return 0

    return 1

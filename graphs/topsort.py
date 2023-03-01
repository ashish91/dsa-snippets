import heapq
class Solution:
  # @param A : integer
  # @param B : list of list of integers
  # @return a list of integers
  def solve(self, A, B):
    graph = dict()

    indeg = [0]*(A+1)
    for node in range(1,A+1):
      graph[node] = []

    for edge in B:
      graph[edge[0]].append(edge[1])
      indeg[edge[1]] += 1

    h = []
    for node in range(1,A+1):
      if indeg[node] == 0:
        h.append(node)
    heapq.heapify(h)
    topsort = []
    vis = [False]*(A+1)
    while len(h) > 0:
      node = heapq.heappop(h)
      vis[node] = True
      topsort.append(node)

      for nei in graph[node]:
        if not vis[nei]:
          indeg[nei] -= 1
          if indeg[nei] == 0:
            heapq.heappush(h,nei)

    return topsort

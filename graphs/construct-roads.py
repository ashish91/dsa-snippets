from collections import defaultdict
class Solution:
  # @param A : integer
  # @param B : list of list of integers
  # @return an integer
  def solve(self, N, edges):
    graph = defaultdict(list)

    for u,v in edges:
      graph[u].append(v)
      graph[v].append(u)

    color = [-1]*(N+1)
    q = [1]
    color[1] = 0
    while len(q) > 0:
      curr = q.pop(0)

      for nei in graph[curr]:
        if color[nei] == color[curr]:
          return 0
        elif color[nei] == -1:
          color[nei] = color[curr]^1
          q.append(nei)

    ones = 0
    zeroes = 0
    for i in range(1,len(color)):
      v = color[i]
      if v == 1:
        ones += 1
      elif v == 0:
        zeroes += 1

    return (ones*zeroes - len(edges))%(10**9 + 7)

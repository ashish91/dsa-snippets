from collections import defaultdict
import heapq
class Solution:
  # @param A : integer
  # @param B : list of list of integers
  # @return an integer
  def solve(self, N, edges):
    graph = defaultdict(list)
    for u,v,w in edges:
      graph[u].append((v,w))
      graph[v].append((u,w))

    def dijkstra(src, graph, dist, exclude):
      h = [(0,src)]
      for i in range(N+1):
        dist[i] = float('infinity')
      dist[src] = 0

      vis = set()
      vis.add(src)
      heapq.heapify(h)
      while len(h) > 0:
        w,node = heapq.heappop(h)

        for nei, nei_w in graph[node]:
          if (node,nei) not in exclude:
            dist[nei] = min(dist[nei], dist[node]+nei_w)
            if nei not in vis:
              heapq.heappush(h,(dist[nei], nei))
              vis.add(nei)
    
    excluded = set()
    dist = [float('infinity')]*(N+1)
    min_cycle = float('infinity')
    for node in range(1,N+1):
      for nei, nei_w in graph[node]:
        edge = (node,nei)

        if edge not in excluded:
          excluded.add((node,nei))
          excluded.add((nei,node))

          exclude = set()
          exclude.add((node,nei))
          exclude.add((nei,node))

          dijkstra(node,graph,dist, exclude)

          min_cycle = min(min_cycle, dist[nei]+nei_w)

    return min_cycle

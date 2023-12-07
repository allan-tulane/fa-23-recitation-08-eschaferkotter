from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  def sspathhelper(visited, frontier):
    if len(frontier) == 0:
      return visited
    else:
      distance, edges, node = heappop(frontier)
      if node in visited:
        return sspathhelper(visited, frontier)
      else:
        visited[node] = (distance, edges)
        for neighbor, weight in graph[node]:
          heappush(frontier, (distance+weight, edges+1, neighbor))
        return sspathhelper(visited, frontier)

  frontier = []
  heappush(frontier, (0,0,source))
  visited = dict()
  return sspathhelper(visited, frontier)
  
def bfs_path(graph, source):
    def bfshelper(visited, frontier, parent):
      if len(frontier) < 1:
        return parent
      else:
        node = frontier.popleft()
        visited.add(node)
        for i in graph[node]:
          if i not in visited and i not in frontier:
            parent[i] = node
            frontier.append(i)
        return bfshelper(visited, frontier, parent)

    parent = dict()
    frontier = deque()
    frontier.append(source)
    visited = set()
    return bfshelper(visited, frontier, parent)

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  if destination in parents:
    return get_path(parents, parents[destination]) + parents[destination]
  else:
    return ""

# program yang ke 3
def uniform_cost_search(goal, start):
  global graph,cost
  answer =[]

  queue =[]

  for i in range(len(goal)):
    answer.append(10**8)
    queue.append([0, start])
    visited ={}
    count = 0
    while (len(queue) >0):
      queue = sorted(queue)
      p = queue[-1]

      del queue[-1]
      p[0] *= -1
      if (p[1] in goal):
        index = goal.idex(p[1])
      if (answer[index] == 10**8):
        coun += 1
      if (answer[index] > p[0]):
        answer[index] = p[0]
      del queue[-1]
      queue = sorted(queue)
      if (count == len(goal)):
        return answer
      if (p[1]not in visited):
        for i in range(len(graph[p[1]])):
          queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][1]])
          visited[p[1]] = 1
          return answer
      if __name__ == '__main__':
        graph,cost = [[]for i in range(8)],{}

        graph[0].append(1)
        graph[0].appned(3)
        graph[3].appned(1)
        graph[3].appned(6)
        graph[3].appned(4)
        graph[1].appned(6)
        graph[4].appned(2)
        graph[4].appned(5)
        graph[2].appned(1)
        graph[5].appned(2)
        graph[5].appned(6)
        graph[6].appned(4)

        cost[{0, 1}] = 2
        cost[{0, 3}] = 5
        cost[{1, 6}] = 1
        cost[{3, 1}] = 5
        cost[{3, 6}] = 6
        cost[{3, 4}] = 2
        cost[{2, 1}] = 4
        cost[{4, 2}] = 4
        cost[{4, 5}] = 3
        cost[{5, 2}] = 6
        cost[{5, 6}] = 3
        cost[{6, 4}] = 7

        goal = []
        goal.append(6)
        answer = uniform_cost_search(goal, 0)
        print("minimun cost from 0 to 6 is = ", answer[0])

# progran ke 4
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

    def IDDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if self.DLS(src, target, i):
                return True
        return False

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 4)
g.addEdge(1, 3)
g.addEdge(1, 5)
g.addEdge(2, 6)

target = 6
maxDepth = 3
src = 0

if g.IDDFS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
else:
    print("Target is NOT reachable from source within max depth")

#program ke lima (5)
class AdjacentNode:

    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class BidirectionalSearch:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

        self.src_queue = []
        self.dest_queue = []

        self.src_visited = [False] * self.vertices
        self.dest_visited = [False] * self.vertices

        self.src_parent = [None] * self.vertices
        self.dest_parent = [None] * self.vertices

    def add_edge(self, src, dest):
        node = AdjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def bfs(self, direction='forward'):
        if direction == 'forward':
            current = self.src_queue.pop(0)
            connected_node = self.graph[current]

            while connected_node:
                vertex = connected_node.vertex

                if not self.src_visited[vertex]:
                    self.src_queue.append(vertex)
                    self.src_visited[vertex] = True
                    self.src_parent[vertex] = current

                connected_node = connected_node.next
        else:
            current = self.dest_queue.pop(0)
            connected_node = self.graph[current]

            while connected_node:
                vertex = connected_node.vertex

                if not self.dest_visited[vertex]:
                    self.dest_queue.append(vertex)
                    self.dest_visited[vertex] = True
                    self.dest_parent[vertex] = current

                connected_node = connected_node.next

    def is_intersecting(self):
        for i in range(self.vertices):
            if self.src_visited[i] and self.dest_visited[i]:
                return i

        return -1

    def print_path(self, intersecting_node, src, dest):
        path = []
        path.append(intersecting_node)
        i = intersecting_node

        while i != src:
            path.append(self.src_parent[i])
            i = self.src_parent[i]

        print("*****path*****")
        path = list(map(str, path))

        print(' '.join(path))

    def bidirectional_search(self, src, dest):
        self.src_queue.append(src)
        self.src_visited[src] = True
        self.src_parent[src] = -1

        self.dest_queue.append(dest)
        self.dest_visited[dest] = True
        self.dest_parent[dest] = -1

        while self.src_queue and self.dest_queue:
            self.bfs(direction='forward')

            self.bfs(direction='backward')

            intersecting_node = self.is_intersecting()
            if intersecting_node != -1:
                print(f"path exists between {src} and {dest}")
                print(f"intersecting at : {intersecting_node}")
                self.print_path(intersecting_node, src, dest)
                exit(0)

        return -1

if __name__ == '__main__':
    n = 15
    src = 0
    dest = 6

    graph = BidirectionalSearch(n)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 8)
    graph.add_edge(8, 9)
    graph.add_edge(8, 10)
    graph.add_edge(9, 11) 
    graph.add_edge(9, 12) 
    graph.add_edge(10, 13) 
    graph.add_edge(10, 14) 

    
    out = graph.bidirectional_search(src, dest)

    if out == -1:
      print(f"path does mot exist bet ween {src} and {dest}")
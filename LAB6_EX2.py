class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_vertex2(self, vertex):
        self.vertices[vertex.name] = vertex

    def add_edge(self, u, v, weight=1):
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight

    def add_edge2(self, u, v):
        self.vertices[u].add_neighbor(v)
        self.vertices[v].add_neighbor(u)

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j],' ', end='')
            print(' ')

    def print_graph2(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

edges = ['AB', 'AC', 'AF','CD', 'DE','EF']
print("==================")
print("Adjacency matrix")
print("------------------")
print("  A  B  C  D  E  F")
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('G')):
    g.add_vertex(Vertex(chr(i)))
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
g.print_graph()
print("==================")
print()
print("==================")
print("Adjacency list")
print("------------------")
for i in range(ord('A'), ord('G')):
    g.add_vertex2(Vertex(chr(i)))
for edge in edges:
    g.add_edge2(edge[:1], edge[1:])
g.print_graph2()
print("==================")
print()
print("=====================================")
print("Edges list")
print("-------------------------------------")
print(edges)
print("=====================================")
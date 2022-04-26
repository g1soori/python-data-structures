class Graph():
    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,": ", self.adj_list[vertex])
    
    def add_edge(self,vert1, vert2):
        if vert1 in self.adj_list.keys() and vert2 in self.adj_list.keys():
            self.adj_list[vert1].append(vert2)
            self.adj_list[vert2].append(vert1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

my_graph = Graph()
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_vertex(3)
my_graph.add_edge(4,5)
my_graph.add_edge(4,3)
my_graph.print_graph()
print("after remove vertex")
my_graph.remove_vertex(3)
my_graph.print_graph()
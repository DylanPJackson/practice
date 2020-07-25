class Graph:
    # Allows for unidirectional and bidirectional graphs
    def __init__(self, nodes = {}):
        self.nodes = nodes # This is the adjacency list

    def __repr__(self):
        return str(self.nodes) 

    def insert(self, val, connections = None):
        self.nodes[val] = connections
        if connections is None:
            return
        for con in connections:
            n_val = con[0]
            rel = con[1] # Relationship. 0 is uni, 1 is bi.
            if rel == 1:
                if self.nodes[n_val] is None:
                    self.nodes[n_val] = [val]
                else:
                    self.nodes[n_val] += [val]
    
    def update(self, val, connections):
        """
            Updates connections for a given node 
        """
        for con in connections:
            n_val = con[0]
            rel = con[1]
            if rel == 0:
                if self.nodes[n_val] is None:
                    if self.nodes[val] is None:
                        self.nodes[val] = [n_val]
                    else:
                        self.nodes[val] += [n_val] 
                else:
                    self.nodes[n_val].remove(val)
            else:
                if self.nodes[n_val] is None:
                    self.nodes[n_val] = [val]
                else:
                    if not(val in self.nodes[n_val]):
                        self.nodes[n_val] += [val]
                if self.nodes[val] is None:
                    self.nodes[val] = [n_val]
                else:
                    if not(n_val in self.nodes[val]):
                        self.nodes[val] += [n_val]

    def delete(self, val):
        cons = self.nodes[val]
        if cons is None:
            self.nodes.pop(val, None)
        else:
            for n_val in cons:
                try:
                    self.nodes[n_val].remove(val)
                except:
                    pass 
        self.nodes.pop(val, None)
        
def main():
    graph = Graph()
    node_1 = 1
    node_2 = 2
    node_3 = 3
    graph.insert(node_1)
    graph.insert(node_2)
    print(graph)
    graph.delete(node_1)
    print(graph)
    graph.insert(node_1)
    print(graph)
    graph.update(node_2, [(1,0)])
    graph.update(node_1, [(2,1)])
    graph.delete(node_1)
    print(graph)

main()

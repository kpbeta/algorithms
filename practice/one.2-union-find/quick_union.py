from union_find import UnionFindInterface

class QuickUnion(UnionFindInterface):
    
    nodes = []
    
    def __init__(self, size):
        self.nodes=super().init_array(size)
    
    def union(self, node_a, node_b):
        a=self.root(node_a)
        b=self.root(node_b)
        self.nodes[a]=b
    
    def root(self, node):
        while self.nodes[node] != node:
            node=self.nodes[node]
        return node
    
    def find(self, node_a, node_b):
        return self.root(node_a) == self.root(node_b)
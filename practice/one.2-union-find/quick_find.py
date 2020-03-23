from union_find import UnionFindInterface

class QuickFind(UnionFindInterface):
    
    nodes = []
    
    def __init__(self, size):
        self.nodes=super().init_array(size)
        
    def union(self, node_a, node_b):
        if not self.find(node_a, node_b):
            to_replace=self.nodes[node_a]
            to_fill=self.nodes[node_b]
            for i in range(0, len(self.nodes)):
                if self.nodes[i]==to_replace:
                    self.nodes[i]=to_fill
    
    def find(self, node_a, node_b):
        if self.nodes[node_a] == self.nodes[node_b]:
            return True
        return False
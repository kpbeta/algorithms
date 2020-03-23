from abc import ABC, ABCMeta, abstractmethod
import numpy as np

class UnionFindInterface(ABC):
    
    def init_array(self,size):
        return np.array(range(0, size))
    
    @abstractmethod
    def union(self, node_a, node_b):
        pass
    
    @abstractmethod
    def find(self, node_a, node_b):
        pass



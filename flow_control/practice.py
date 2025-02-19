class UnionFind:
    def __init__(self, vertices: int):
        self.parents = [i for i in range(vertices)]
        self.rank = [1] * vertices
        
    def find(self, index):
        result = index
        
        # find parent index, setting all child/descendent index to parent index on the way
        while result != self.parents[result]:
            self.parents[result] = self.parents[self.parents[result]]
            result = self.parents[result]
        
        return result 
    
    def union(self, v1, v2):
        parent1, parent2 = self.find(v1), self.find(v2)
        
        if parent1 == parent2:
            return 0

        
        if self.rank[parent2] > self.rank[parent1]:
            self.parents[parent1] = parent2
            self.ranks[parent2] += self.ranks[parent1]
            
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += self.ranks[parent2]
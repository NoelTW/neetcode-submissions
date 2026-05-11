class DSU:
    def __init__(self, elements):
        self.parents = {x: x for x in elements}
        self.sizes = {x: 1 for x in elements}
        self.max_size = 1 if elements else 0

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        if y not in self.parents:
            return
        
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.sizes[px] < self.sizes[py]:
                px, py = py, px
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
            if self.sizes[px] > self.max_size:
                self.max_size = self.sizes[px]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        unique_nums = set(nums)
        dsu = DSU(unique_nums)
        
        for x in unique_nums:
            if x + 1 in unique_nums:
                dsu.unite(x, x + 1)
                
        return dsu.max_size
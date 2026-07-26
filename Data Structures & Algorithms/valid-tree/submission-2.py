class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.comps = n
        par = [i for i in range(n)]
        size = [1] * n
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb: return False
            self.comps -= 1
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            par[pb] = pa
            size[pa] += size[pb]
            return True

        def find(a):
            if a != par[a]:
                par[a] = find(par[a])
            return par[a]
        for i, j in edges:
            if not union(i, j): return False
        
        return self.comps == 1
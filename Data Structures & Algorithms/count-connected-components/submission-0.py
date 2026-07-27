class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        size = [0] * n
        self.num_com = n
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            par[pb] = pa
            size[pa] += size[pb]
            self.num_com -= 1
            return True

        def find(a):
            if a != par[a]:
                par[a] = find(par[a])
            return par[a]

        for a, b in edges:
            union(a, b)
        print(self.num_com)
        return self.num_com
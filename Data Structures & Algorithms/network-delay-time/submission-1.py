class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 无法保证当一个节点的距离被更新（变得更小）时，它的邻居也能被重新处理。
        adj_ls = defaultdict(list)
        for t in times:
            adj_ls[t[0]].append((t[1], t[2]))
       
        print(adj_ls)
        # time_ls = {i: float('inf') for i in range(1, n+1)}
        # time_ls[k] = 0

        pq = [(0, k)] 
        # queue = []
        visited = set()
        # queue.append(k)
        # visited.append(k)
        res = 0
        while pq:
            t1, node1 = heapq.heappop(pq)
            print(node1)
            # if node1 not in adj_ls: continue
            if node1 in visited: continue
            visited.add(node1)
            res = t1
            for node2, t2 in  adj_ls[node1]:
                if node2 not in visited:
                    heapq.heappush(pq,(t1 + t2, node2))

            
        return res if len(visited) == n else -1

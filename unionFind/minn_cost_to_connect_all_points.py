class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [-1] * len(points)
        
        def find(u):
            temp_u = u
            while parents[u] >= 0:
                u = parents[u]
            
            while parents[temp_u] >= 0:
                parents[temp_u], temp_u = u, parents[temp_u]
            return u
        
        def union(u, v):
            p_u, p_v = find(u), find(v)
            if p_u == p_v:
                return False
            if parents[p_u] <= parents[p_v]:
                parents[p_v] += parents[p_u]
                parents[p_u] = p_v
            else:
                parents[p_u] += parents[p_v]
                parents[p_v] = p_u
            return True
        
        heap = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                heapq.heappush(heap, (abs(x1-x2) + abs(y1-y2), i, j))
        
        cost = 0
        while heap:
            c, i, j = heapq.heappop(heap)
            if union(i, j):
                cost += c
        return cost

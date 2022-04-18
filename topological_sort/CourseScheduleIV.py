class Solution:
    def make_pre_set(self, graph, numCourses):
        in_digree = {i:0 for i in range(numCourses)}
        
        for node in graph:
            for nbr in graph[node]:
                in_digree[nbr] += 1
            
        pre_set = {i:set() for i in range(numCourses)}
        que = deque()
        
        for node in in_digree:
            if in_digree[node] == 0:
                que.append(node)
                
        while len(que) > 0:
            cur = que.popleft()
            for nbr in graph[cur]:
                pre_set[nbr].add(cur)
                for pre in pre_set[cur]:
                    pre_set[nbr].add(pre)
                
                in_digree[nbr] -= 1
                if in_digree[nbr] == 0:
                    que.append(nbr)
                    
        return pre_set
    
    def checkIfPrerequisite(self, numCourses: int, eages: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = {i:[] for i in range(numCourses)}
        
        for start, end in eages: 
            graph[start].append(end)
        pre_set = self.make_pre_set(graph, numCourses)
        
        ans = []
        for pre, course in queries:
            is_pre  = pre in pre_set[course]
            ans.append(is_pre)
            
        return ans 

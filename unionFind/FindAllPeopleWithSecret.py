class Solution:
    def find(self, node, parents):
        if parents[node] == node:
            return node
        
        parents[node] = self.find(parents[node], parents)
        return parents[node]
    
    def union(self, a, b, parents, size):
            
        root_a = self.find(a, parents)
        root_b = self.find(b, parents)
        
        if root_a == root_b:
            return
        if size[root_b] > size[root_a]:
            root_a, root_b = root_b, root_a
        
        parents[root_b] = root_a
        size[root_a] += size[root_b]
            
    def add_people_to_the_society(self, eages, secret_society):
        
        parents = {};  size = {} 
        
        for start, end, _ in eages:
            
            if start not in parents:
                parents[start] = start; size[start] = 1
                
            if end not in parents:
                parents[end] = end; size[end] = 1
                
            self.union(start, end, parents, size)
         
        secret_roots = set()
        for node in parents:
            if node in secret_society:
                root = self.find(node, parents)
                secret_roots.add(root)
        
        for node in parents:
            if node in secret_society:
                continue
                
            root = self.find(node, parents)
            if root in secret_roots:
                secret_society.add(node)
        
    def findAllPeople(self, n: int, meet: List[List[int]], firstPerson: int) -> List[int]:
        meet.sort(key = lambda x:x[2])
        secret_society = {0, firstPerson}
        
        left = 0
        right = 0
        while right < len(meet):
            while right + 1 < len(meet) and meet[right+1][2] == meet[right][2]:
                right += 1
                
            self.add_people_to_the_society(meet[left:right+1], secret_society)
            right += 1
            left = right
        
        return secret_society

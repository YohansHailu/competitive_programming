class Solution:
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        
        if self.size[a_root] < self.size[b_root]:
            self.parent[a_root] = b_root
            self.size[b_root] += self.size[a_root]
        else:
            self.parent[b_root] = a_root
            self.size[a_root] += self.size[b_root]
        
    def accountsMerge(self, acc: List[List[str]]) -> List[List[str]]:
        self.parent = {i:i for i in range(len(acc))}
        self.size = {i:1 for i in range(len(acc))}
        
        location = {}
        for i in range(len(acc)):
            for j in range(1, len(acc[i])):
                
                email = acc[i][j]
                if email not in location:
                    location[email] = []
                location[email].append(i)
                
        ## make unions         
        for email in location:
            arr = location[email]
            for i in range(len(arr)-1):
                self.union(arr[i], arr[i+1])
        
        # finish here
        result = {}
        for i in range(len(acc)):
            i_root = self.find(i) 
            if i_root not in result:
                result[i_root] = acc[i].copy()
            else:
                result[i_root] += acc[i][1:]
            
        res = []   
        for row in result.values():
            new_row = [row[0]] + sorted(set(row[1:]))
            res.append(new_row)
            
        return res

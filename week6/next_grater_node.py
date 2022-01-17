class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        inc_stack = [] ## elemets will be val,index
        g_dict = dict()
        
        index = 0
        while head != None:
            while len(inc_stack) > 0 and inc_stack[-1][0] < head.val:
                g_dict[inc_stack.pop()[1]] = head.val
            inc_stack.append([head.val,index])
            
            head = head.next
            index += 1
         
        for i in inc_stack:
            g_dict[i[1]] = 0
        
        ans = [0]*len(g_dict)
        for i in g_dict.keys():
            ans[i] = g_dict[i]
        
        return ans

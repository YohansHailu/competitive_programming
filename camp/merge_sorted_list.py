class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ## we have an answer
        ##  heap with touple and index in the lists
        ## we append and we go forthun push to heap
        
        minh = []
        for i in range(len(lists)):
            if lists[i] != None:
                heappush(minh, (lists[i].val,i))
        
        dumby = ListNode()
        cur = dumby
        while len(minh) > 0:
            poped = heappop(minh)
            cur.next = ListNode(poped[0])
            cur = cur.next 
            
            index = poped[1]
            if lists[index].next != None:
                lists[index] = lists[index].next
                heappush(minh, (lists[index].val,index) )
                
        
        return dumby.next 

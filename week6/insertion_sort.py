class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr  = []
        
        ans  = ListNode(78)
        cur = ans
        while head  != None:
            arr.append(head.val)
            head = head.next
        arr.sort()
        
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        return ans.next
        

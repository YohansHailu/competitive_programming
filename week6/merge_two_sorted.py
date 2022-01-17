class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      
        ans = ListNode()
        
        cur = ans
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.next = list1
                temp = list1.next
                list1.next = list2
                list1 = temp
                cur = cur.next
            else:
                cur.next = list2
                temp = list2.next
                list2.next = list1
                list2 = temp
                cur = cur.next
        if list1 != None:
            cur.next = list1
        if list2 != None:
            cur.next = list2
        
        return ans.next
                

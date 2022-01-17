class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(0); # dummy
        cur = ans
        c = 0
        s = 0
        while l1 != None and l2 != None:
            s = l1.val + l2.val + c
            c = s//10
            s = s%10
            ans.next = ListNode(s)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            s = l1.val + c
            c = s//10
            s = s%10
            ans.next = ListNode(s)
            ans = ans.next
            l1 = l1.next
        
        while l2 != None:
            s = l2.val + c
            c = s//10
            s = s%10
            ans.next = ListNode(s)
            ans = ans.next
            l2 = l2.next
        if(c != 0):
            ans.next = ListNode(c)
            ans = ans.next
            
        return cur.next

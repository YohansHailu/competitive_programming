class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def helper(head,end):
            ans = True
            if end.next != None:
                ans , head = helper(head,end.next)
            
            return [head.val == end.val and ans ,head.next]
        
        end = head
        return helper(head,end)[0]
        

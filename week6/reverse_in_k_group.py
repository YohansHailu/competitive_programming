from collections import deque
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_stack = deque()
        ans  = ListNode(3213) # dumb node
        cur = ans
        while head != None:
            while head != None and len(node_stack) < k:
                temp = head.next
                head.next = None
                node_stack.append(head)
                head = temp
            
            if len(node_stack) < k:
                while len(node_stack) > 0:
                    poped_node = node_stack.popleft()
                    cur.next = poped_node
                    cur = cur.next    
                
            while len(node_stack) > 0:
                poped_node = node_stack.pop()
                cur.next = poped_node
                cur = cur.next

        return ans.next
        

class MyQueue:

    def __init__(self):
        self.mystack = []
        

    def push(self, x: int) -> None:
        self.mystack.append(x)
        

    def pop(self) -> int:
        x=self.mystack.pop(0)
        return x
        

    def peek(self) -> int:
        return self.mystack[0]
        

    def empty(self) -> bool:
        return len(self.mystack)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

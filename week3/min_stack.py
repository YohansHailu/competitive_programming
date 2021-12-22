class MinStack:

    def __init__(self):
        self.mystack = list()
        

    def push(self, val: int) -> None:
        self.mystack.append(val)

    def pop(self) -> None:
        self.mystack.pop()
        

    def top(self) -> int:
        return self.mystack[-1]
        

    def getMin(self) -> int:
        m = self.mystack[0]
        for el in self.mystack:
            m = min(m,el)
        return m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

 def fib_helper(self, n, memory):
        if memory[n] != -1:
            return memory[n]
        
        ans = self.fib_helper(n-1, memory) + self.fib_helper(n-2, memory)
        memory[n] = ans
        
        return ans
    
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        memory = [-1]*(n+1)
        memory[0] = 0
        memory[1] = 1
        
        return self.fib_helper(n, memory)
        

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        isN = False;

        
        left = 0
        right = 0
        
        
        while left<len(s):
            if s[left] == ' ':
                left+=1
            elif 48 <= ord(s[left])<=57:
                break
            elif s[left] == "-":
                isN = True
                if left+1<len(s) and 48 <= ord(s[left+1])<=57:
                    left+=1
                else: return 0
            elif s[left] == '+':
                if left+1<len(s) and 48 <= ord(s[left+1])<=57:
                    left+=1
                else: return 0
            else: return 0
        
       
        right = left
        while right<len(s) and 48<= ord(s[right])<=57:
            right+=1
        
        result = 0;
        s = s[left:right]
        for i in range(len(s)):
            result += (ord(s[i])-48) * 10**(len(s)-1-i)
            
        if isN == True:
            result *= -1;
            
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        
        return result
            
            

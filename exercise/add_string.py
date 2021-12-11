class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1);
        num2 = list(num2);
        num1.reverse();
        num2.reverse();
        
        slen = len(num1) if len(num1) < len(num2) else len(num2)
        
        carry = 0
        isum=0
        sum_string = []

        for i in range(slen):
            isum = int(num1[i]) + int(num2[i]) + carry
            carry = isum//10;
            isum %=10;
            
            sum_string+=str(isum)
        
        if (len(num1) - len(num2)) == 0 and carry ==1:
            sum_string+=str(carry)
        
        elif (len(num1) - slen) > 0:
            isum = int(num1[slen]) + carry;
            sum_string+=str(isum)
            sum_string+= num1[slen+1:]
        elif(len(num2) - slen) > 0:
            isum = int(num2[slen]) + carry;
            sum_string+=str(isum)    
            sum_string += num2[slen+1:]
        
        sum_string.reverse()
        sum_string="".join(sum_string)
        return sum_string

   def compress(self, chars: List[str]) -> int:
        # head variable and index pointer
        # head at last will give the length 
        # head will be the length
        
        # but the head to a variabl
        # move index untile the end counting
        # add to the next and move the head if greate than one
        # put the next value to head and move the head
        # just move the head
        
        
       
        head = 0
        i = head 
        count = 0
        while head < len(chars) and i < len(chars):
            chars[head] = chars[i] 
            hval = chars[head]
            
            count = 0
            while i < len(chars) and chars[i] == hval:
                i += 1
                count += 1
                
            if count > 1:
                n = str(count)
                for t in range(len(n)):
                    chars[head+t+1] = n[t] 
                head += len(n)+1
            else:
                head += 1
                
        return head

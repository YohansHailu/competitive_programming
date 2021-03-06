class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        left = 0
        right = len(numbers) - 1
        
        while right > left:
            
            s = numbers[right] + numbers[left]
            
            if s == target:
                return [left+1,right+1]
            
            if s < target:
                left += 1
            elif s > target:
                right -= 1
        
        return []
            
        

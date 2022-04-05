class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        for i in range(len(word)):
            if word[i] in ['a', 'e','i', 'o', 'u']:
                res += len(word)
                res += i * (len(word) - i - 1)
                
        return res

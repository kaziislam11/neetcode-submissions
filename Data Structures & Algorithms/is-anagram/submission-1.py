class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        
        for letter in s:
            countS[letter] = countS.get(letter, 0) + 1
        
        for letter in t:
            countT[letter] = countT.get(letter, 0) + 1
        
        return countS == countT
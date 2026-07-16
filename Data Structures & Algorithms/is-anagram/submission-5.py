class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char in count:
                count[char] -= 1
            else:
                count[char] = -1

        return all(v==0 for v in count.values())

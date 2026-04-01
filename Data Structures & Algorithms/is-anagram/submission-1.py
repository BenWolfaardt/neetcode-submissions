class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sSorted = sorted(s)
        tSorted = sorted(t)

        if sSorted == tSorted:
            return True
        return False
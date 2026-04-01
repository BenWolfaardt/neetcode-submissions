class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = sorted(nums)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return True
        return False
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for _, count in c.items():
            if count > 1:
                return True
        return False
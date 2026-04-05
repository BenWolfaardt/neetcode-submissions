from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)

        for num in nums:
            dictionary[num] += 1

        # todo sort list in order of key frequencies and slice it to get k
        sorted_list = sorted(dictionary, key=dictionary.get, reverse=True)
        return sorted_list[:k]

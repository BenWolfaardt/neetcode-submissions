class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if 1 > len(strs) | len(strs) > 1000:
            return [[""]]
        
        seen = set()
        itteration_set = []
        response: List[List[str]] = []

        for i, string in enumerate(strs):
            if len(string) > 100:
                return [[""]]
            sort_i = sorted(string)

            if strs[i] not in seen:
                itteration_set.append(strs[i])
                seen.add(strs[i])
            else: 
                continue

                # TODO: optimise by not double checking
            for j in range(i+1, len(strs)):
                sort_j = sorted(strs[j])

                if sort_i == sort_j:
                    itteration_set.append(strs[j])
                    seen.add(strs[j])

            response.append(itteration_set)
            itteration_set = []

        return response

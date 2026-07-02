from itertools import permutations
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = [False] * len(strs)

        OG = []
        for i in range(len(strs)):
            if seen[i]:
                continue
            group = [strs[i]]
            seen[i] =  True
            
            for j in range(i+1, len(strs)):
                if not seen[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    seen[j] = True
            OG.append(group)
        return OG
        
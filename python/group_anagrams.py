class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= DefaultDict(list)
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            d[s].append(strs[i])
        return [d[key] for key in d]

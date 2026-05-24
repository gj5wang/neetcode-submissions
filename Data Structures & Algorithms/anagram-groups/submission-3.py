class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(0, len(strs)):
            if "".join(sorted(strs[i])) not in seen.keys():
                seen["".join(sorted(strs[i]))] = [strs[i]]
            else:
                seen["".join(sorted(strs[i]))].append(strs[i])
        return list(seen.values())
        
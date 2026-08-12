class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s)) #join makes list back to string
            res[sortedS].append(s)#the sortedS is the key
        return list(res.values())
        
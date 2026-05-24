class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        sorted_seen = dict(sorted(seen.items(), key = lambda x: x[1], reverse = True))
        return list(sorted_seen.keys())[:k]


#use the has map dictionary
#key: the element, value: the number of times it occurs
#sort by value
#output the first k keys in the sorted dictionary
        
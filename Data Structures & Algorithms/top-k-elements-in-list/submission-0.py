class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        #step 1: count frequencies
        freq_map = Counter(nums)#counter is basically a dictinary listing how many times each element of the list occurs in descending order
        #the most frequent element occurs first

        #step 2: Sort by frequency(descending) and take top k
        #sorted() returns list of keys sorted by their frequency
        return sorted(freq_map.keys(), key = lambda x : freq_map[x])[:k]


        
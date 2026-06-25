class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        for val in hash.values():
            if val > 1:
                return True
                Break
            else:
                continue
        
        return False
        
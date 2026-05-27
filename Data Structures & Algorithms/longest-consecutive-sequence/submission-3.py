class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert to set, check each number in the set
        #check if the first number have a consecutive number smaller, if so
        #srart checking with that number(to see if it has a smaller consecutive)
        #if no start going up and find the number of consecutive nubers

        NumSet = set(nums)
        FindMax = set()
        for num in NumSet:
            if num - 1 not in NumSet:
                length = 1

                while (num + length) in NumSet:
                    length += 1
            
                FindMax.add(length)
        
        if FindMax == set():
            return 0
        else:
            return max(FindMax)

        
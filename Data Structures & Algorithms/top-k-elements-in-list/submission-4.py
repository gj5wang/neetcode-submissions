class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use hash map
        #key = the number
        #value = the number's count
        #sort by value
        #the value of keys indexed upto k - 1 appended into list

        lst = defaultdict(int)

        for num in nums:
            lst[num] += 1
        
        sorted_lst = sorted(lst.items(),key = lambda x: x[1], reverse = True)
        output = []
        for i in range (k): #k is not included
            output.append(sorted_lst[i][0])
        
        return output
        
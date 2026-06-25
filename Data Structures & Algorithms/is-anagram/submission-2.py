class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use hash map, figure out how many times each letter occurs

        s_dict = {}
        t_dict = {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        #orders in hashmap don't matter, they are sorted by keys
        if s_dict == t_dict:
            return True
        else:
            return False
        

        
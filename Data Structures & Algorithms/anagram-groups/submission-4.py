class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #take it as a set, hash map out all the letters contained
        hash = {}

        for s in strs:
            key = "".join(sorted(s))#make it bacl to string

            if key not in hash.keys():
                hash[key] = [s]
            else:
                hash[key].append(s)

        output = []

        for i in hash.keys():
            output.append(hash[i])
        
        return output


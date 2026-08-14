class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 # remember where it starts

        while i < len(s):
            j = i # j keep move forward to find "#" to basically know how long the length is

            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # j = #, so find the len
            
            result.append(s[j+1:j+1+length])
            i = j + length + 1 #update the start index
        
        return result
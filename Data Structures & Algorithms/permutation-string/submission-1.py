class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0 

       #Count characters of s1
       #Slide a window of size len(s1) over s2
       #Compare counts

        s1_count = Counter(s1)
        window_count = Counter()

        for right in range(len(s2)):
            window_count[s2[right]] += 1
            
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
            
            if window_count == s1_count:
                return True
        
        return False
       

        
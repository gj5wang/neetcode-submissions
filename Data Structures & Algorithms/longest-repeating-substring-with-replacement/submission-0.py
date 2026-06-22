class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #overall logic: use sliding window
        #1. move right forward one character at a time
        #2. count how many of each character are in the current window
        #3. find the most common character count(max_count)
        #4. Everything other than that character would need to be replaced
        #5. if replacements needed exceed k, move left forward to shrink the window
        #6. track the largest valid window size
        left = 0
        counts = {}#dictonary, each char in s carries a value of how many times it appears
        max_count = 0
        longest = 0

        for right in range(len(s)):
            #looks up how many times the character has appeared in the current window
            #if already exist in counts, return its value
            #if it does not exist yet, return 0 
            #+1 for thsi new occurence
            counts[s[right]] = counts.get(s[right], 0) + 1

            max_count = max(max_count, counts[s[right]])

            while (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest

            
        
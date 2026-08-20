class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create a new string that only contains the alphabets and the numbers
        #compare the string itself and its reversed, if same return true else false
        new = ""
        for c in s:
            if c.isalnum():
                new += c.lower()
        return new == new[::-1]        
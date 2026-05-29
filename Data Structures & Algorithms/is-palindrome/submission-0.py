class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():#check if a character is a letter or number
                newStr += c.lower() #since python is case sensitive

        return newStr == newStr[::-1]

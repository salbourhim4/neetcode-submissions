class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(char for char in s if char.isalnum())
        if strs.lower() == strs[::-1].lower():
            return True
        return False
        
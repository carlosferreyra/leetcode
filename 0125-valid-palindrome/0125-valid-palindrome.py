class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": return True
        out = []
        for char in s:
            if char.isalnum():
                out.append(char.lower())
        return out==out[::-1]
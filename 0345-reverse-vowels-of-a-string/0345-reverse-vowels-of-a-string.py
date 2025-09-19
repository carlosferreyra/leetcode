class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use a list to make the string mutable
        output: list[str] = list(s) 
        
        # Store vowels in a separate list
        vowels_in_s: list[str] = []
        vowels: set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        for char in s:
            if char in vowels:
                vowels_in_s.append(char)
        
        # Now, replace the vowels in the original list, in reverse order
        for i in range(len(output)):
            if output[i] in vowels:
                output[i] = vowels_in_s.pop()
                
        return "".join(output)
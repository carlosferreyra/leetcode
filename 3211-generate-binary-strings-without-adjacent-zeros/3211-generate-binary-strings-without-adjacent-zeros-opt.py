class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        
        res = []
        
        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return
            # Always can add '1'
            backtrack(s + "1")
            # Can add '0' only if previous char is not '0'
            if not s or s[-1] != "0":
                backtrack(s + "0")
        
        backtrack("")
        return res

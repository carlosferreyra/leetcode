from collections import Counter
class Solution:

    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        h=Counter(s)
        hh=Counter(t)
        if h==hh:
            return True
        else:
            return False
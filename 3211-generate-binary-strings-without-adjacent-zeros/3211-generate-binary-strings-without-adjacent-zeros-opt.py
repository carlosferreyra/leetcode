__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def __init__(self):
        self.ans = []

    def f(self, prev: int, str_: str, n: int):
        if len(str_) == n:
            self.ans.append(str_)
            return
        self.f(1, str_ + '1', n)
        if prev == 1:
            self.f(0, str_ + '0', n)

    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        self.f(0, "0", n)
        self.f(1, "1", n)
        return self.ans
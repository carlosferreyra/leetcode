class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for idx in range(1,n+1):
            if idx % 3 == 0 and idx % 5 == 0: out.append("FizzBuzz")
            elif idx % 3 == 0: out.append("Fizz")
            elif idx % 5 == 0: out.append("Buzz")
            else: out.append(str(idx))
        return out
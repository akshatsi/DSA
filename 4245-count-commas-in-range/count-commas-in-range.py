class Solution:
    def countCommas(self, n: int) -> int:
        a = len(str(n))
        total = 0
        if a < 4:
            return 0

        return n - 1000 + 1
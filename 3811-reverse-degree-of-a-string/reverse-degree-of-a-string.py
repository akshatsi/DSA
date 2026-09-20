class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, j in enumerate(s):
            total += (i+1) * (ord('z')- ord(j) + 1)

        return total
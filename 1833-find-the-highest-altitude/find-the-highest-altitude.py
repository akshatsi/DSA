class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        res = [0] * (n + 1)

        for i in range(0, len(gain)):
            res[i + 1] = res[i] + gain[i]

        return max(res)
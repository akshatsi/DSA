class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        s = "123456789"
        l = str(low)
        h = str(high)
        for length in range(len(l), len(h) + 1):
            for start in range(0, 10 - length):
                nums = int(s[start: start + length])
                if low <= nums <= high:
                    ans.append(nums)

        return ans
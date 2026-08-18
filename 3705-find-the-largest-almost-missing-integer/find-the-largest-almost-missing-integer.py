class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        for start in range(len(nums) - k + 1):
            seen = set()

            for i in range(start, start + k):
                seen.add(nums[i])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1
        for num, freq in count.items():
            if freq == 1:
                ans = max(ans, num)

        return ans
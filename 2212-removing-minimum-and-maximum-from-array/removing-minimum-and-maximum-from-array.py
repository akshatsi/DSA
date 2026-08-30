class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))

        l = min(mini, maxi)
        r = max(mini, maxi)

        return min(
            r + 1,
            n - l,
            (l + 1) + (n - r)
        )
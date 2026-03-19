class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        freq = {}
        l = 0
        res = 0

        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            res += (r - l + 1)

        return res
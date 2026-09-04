class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        temp = []

        for i in range(len(nums)):
            temp.append(nums[i])
            maxi = max(temp)
            mini = min(nums[i::])

            if maxi - mini <= k:
                return i

        return -1
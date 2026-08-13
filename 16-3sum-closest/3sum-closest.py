class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                if abs(target - total) < abs(target-res):
                    res = total
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1

        return res
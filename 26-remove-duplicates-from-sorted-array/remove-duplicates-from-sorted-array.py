class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[a] = nums[i+1]
                a+= 1

        return a
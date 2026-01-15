class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''ans = set()
        for i in range(len(nums)):
            hashset = set()
            for j in range (i+1, len(nums)):
                third = -(nums[i]+nums[j])
                if third in hashset:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    ans.add(triplet)
                hashset.add(nums[j])

        return [list(triplets) for triplets in ans]'''

        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left,right = i+1,n-1
            while left < right:
                total = nums[i] + nums [left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return ans

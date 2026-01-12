class Solution(object):
    def majorityElement(self, nums):
        a = len(nums)
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            if value > a / 3:
                result.append(key)

        return result
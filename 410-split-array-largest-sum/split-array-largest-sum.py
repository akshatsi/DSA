class Solution:
    def count_partitions(self, a: int,max_sum: int) -> int:
        partitions = 1  
        subarray_sum = 0

        for num in a:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)  
        high = sum(nums)  

        while low <= high:
            mid = (low + high) // 2
            partitions = self.count_partitions(nums, mid)

            if partitions > k:
                low = mid + 1  
            else:
                high = mid - 1 
        return low
        
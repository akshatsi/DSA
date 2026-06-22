class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        count = 0
        while count != k:
            res = -(heapq.heappop(max_heap))
            count += 1

        return res

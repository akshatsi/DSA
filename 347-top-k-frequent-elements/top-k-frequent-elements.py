class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        my_heap = []
        for key, value in freq.items():
            if len(my_heap) < k:
                heapq.heappush(my_heap, [value, key])
                continue
            

            if value > my_heap[0][0]:
                heapq.heappop(my_heap)
                heapq.heappush(my_heap, [value, key])


        return [my_heap[i][1] for i in range(len(my_heap))]            
            
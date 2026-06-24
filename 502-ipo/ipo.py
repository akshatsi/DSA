class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = []
        for i in range(len(profits)):
            pairs.append([capital[i], profits[i]])

        pairs.sort()
        idx = 0
        max_heap = []
        while k != 0:
            while idx < len(pairs):
                if w < pairs[idx][0]:
                    break
                heapq.heappush(max_heap, -pairs[idx][1])
                idx += 1
            if max_heap:
                w -= heapq.heappop(max_heap)
            else:
                return w
            k -= 1

        return w







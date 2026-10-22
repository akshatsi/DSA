class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if not stones:
            return 0
        a = []
        for i in stones:
            heapq.heappush(a,-i)
        while len(a) > 1:
            x = heapq.heappop(a)
            y = heapq.heappop(a)

            if x != y:
                heapq.heappush(a, (abs(y) - abs(x)))  
            else:
                continue

        if a:
            return abs(a[0])
        else:
            return 0

            


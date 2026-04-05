class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        time = 0

        while maxHeap:
            temp = []
            cycle = n + 1

            i = 0
            while i < cycle and maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1 #cuz count is -ve

                if count < 0:
                    temp.append(count)

                time += 1
                i += 1

            for item in temp:
                heapq.heappush(maxHeap, item)

            if maxHeap:
                time += (cycle - i)

        return time
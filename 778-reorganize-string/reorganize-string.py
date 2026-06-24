class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1

        for key, value in freq.items():
            heapq.heappush(max_heap, [-value, key])

        res = ""
        seat = 0
        while(max_heap):
            student = heapq.heappop(max_heap)
            if seat == 0 or res[seat - 1] != student[1]:
                res += student[1]
                student[0] += 1
                if student[0] < 0:
                    heapq.heappush(max_heap,student)
                seat += 1

            else:
                if not max_heap:
                    return ""
                else:
                    new_student = heapq.heappop(max_heap)
                    res += new_student[1]
                    seat += 1
                    new_student[0] += 1
                    if new_student[0] < 0:
                        heapq.heappush(max_heap,new_student)
                heapq.heappush(max_heap,student)
        return res
        
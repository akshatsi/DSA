import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))

        result = []

        for _ in range(k):
            count, word = heapq.heappop(heap)
            result.append(word)

        return result
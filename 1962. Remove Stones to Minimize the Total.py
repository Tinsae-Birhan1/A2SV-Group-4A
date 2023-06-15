class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        arr = [- i for i in piles]
        heapq.heapify(arr)
        for i in range(k):
            count = heappop(arr)
            x = count // 2
            heappush(arr, x)
        return -sum(arr)
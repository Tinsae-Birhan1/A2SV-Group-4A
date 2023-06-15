class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        heap = [(nums1[i]+nums2[0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            if not heap:
                return res
            s, x, y = heapq.heappop(heap)    
            res.append((nums1[x],nums2[y]))
            y+=1
            if y<m:
                heapq.heappush(heap, (nums1[x]+nums2[y], x, y))
        return res
            
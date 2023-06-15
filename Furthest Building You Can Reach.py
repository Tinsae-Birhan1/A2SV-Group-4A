class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq
        i = 0
        n = len(heights)
        h = []
        l=[]
        s = 0
        t =0
        while i < n-1:
            if heights[i] >= heights[i+1]:
                i+=1
                continue
            gap = heights[i+1]-heights[i]
            s+=gap
            if len(l)<ladders:
                heapq.heappush(l, gap)
                t+=gap
            elif l and l[0] < gap:
                r = heapq.heappushpop(l, gap)
                t+=gap-r
            if s-t > bricks:
                break
            i+=1
        return i

        
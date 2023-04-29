class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        for i in range(len(height)):
            
            for j in range(i,len(height)):
                h=min(height[i], height[j])
                w=abs(height[i]-height[j])
                max_min_area=h*w

                max_area=max(max_area, max_min_area)
        return max_area


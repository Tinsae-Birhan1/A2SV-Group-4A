class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            mins = heights[i]
            for j in range(i, len(heights)):
                if mins < heights[j]:
                    names[i], names[j] = names[j], names[i]
        return names
        
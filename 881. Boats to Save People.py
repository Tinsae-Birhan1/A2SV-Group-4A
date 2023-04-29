class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # boat=0
        # l=0
        # r=len(people)-1
        # people.sort()
        # while l<=r:
        #     rem=limit- people[r]
        #     boat+=1
        #     r-=1
        #     if l<=r and rem>=people[l]:
        #         l+=1
        # return boat
        boat = 0
        people.sort()
        left = 0
        right = len(people)-1
        while right >= left:
            rem = limit - people[right]
            boat += 1
            right -= 1
            if left <= right and rem >= people[left]:
                left+=1
        return boat

        
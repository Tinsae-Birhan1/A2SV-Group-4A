class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        count = []
        comp = skill[0] + skill[-1]
        while right > left:
            if comp == skill[left] + skill[right]:
                count.append((skill[left], skill[right]))
            else:
                return -1
            left +=1
            right -= 1
        sums = 0
        for i in range(len(count)):
            mults = count[i][0] *  count[i][1]
            sums +=mults
        return sums

        
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coll=defaultdict(int)
        for i in bills:
            if i== 5:
                coll[5] += 1
            elif i==10:
                if coll[5] == 0:
                    return False
                coll[5] -= 1
                coll[10] += 1
            elif i==20:
                if coll[10] >= 1 and coll[5] >= 1:
                    coll[10] -= 1
                    coll[5] -= 1
                elif coll[5] >= 3:
                    coll[5] -= 3
                else:
                    return False
        return True
                
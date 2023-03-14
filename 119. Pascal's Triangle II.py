class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex - 1)
        cur = [1]

        for num in range(len(prev) - 1):
            cur.append(prev[num] + prev[num + 1])
        cur.append(1)
        return cur
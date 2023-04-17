class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        
        stack=[]
        for l in range(columns):
            arr=[]
            for r in range(rows):

                arr.append(matrix[r][l])
            stack.append(arr)
        return stack
        
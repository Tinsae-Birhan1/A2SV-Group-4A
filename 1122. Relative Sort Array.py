class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=[]
        for i in arr2:
            while i in arr1:
                arr.append(i)
                arr1.remove(i)

        return(arr+sorted(arr1))


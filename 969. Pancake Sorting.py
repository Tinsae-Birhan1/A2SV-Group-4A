class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i += 1
        
        def sort(i):
            if i < 0:
                return []
            ret = []
            idx = arr.index(i + 1)
            if idx == i:
                return sort(i - 1)
            
            ret.append(idx + 1)
            flip(0, idx)
            ret.append(i + 1)
            flip(0, i)
            return ret + sort(i - 1)
            
            
        return sort(len(arr) - 1)
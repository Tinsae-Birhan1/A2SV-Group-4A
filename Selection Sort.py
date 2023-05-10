 def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            small = i
            for j in range(i+1, n):
                if arr[j] < arr[small]:
                    small = j
            arr[small], arr[j] = arr[j], arr[small]
        return arr
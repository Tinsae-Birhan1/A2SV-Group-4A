def help(  i, arr_n):
    low = 0
    high = n - 1
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr_n[mid] <= i:
            index = mid
            low = mid + 1
        else:
            high = mid - 1
    return index +1


n,m= [int(x) for x in input().split()]
arr_n=[int(x) for x in input().split()]
arr_m=[int(x) for x in input().split()]

arr_n.sort()
for x in arr_m:
    i = help(x, arr_n)
    print(i, end=' ')




# for i in arr_m:
    
#     while low <= high:
#         mid = (low + high) // 2
#         if arr_n[mid] <= i:
#             index = mid
#             low = mid + 1
#         else:
#             high = mid - 1
            
#     print(index + 1, end=' ')





class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # result=set(edges[0]).intersection(edges[1]).pop()
        # return result


        arr =[]
        for i in range(len(edges)):
            for j in range(len(edges[0])):
                arr.append(edges[i][j])
        count = Counter(arr)
        print(count)
        return count.most_common(1)[0][0]


        # dct = {}
        # for i in edges:
        #     for j in i:
        #         if j in dct:
        #             dct[j]+=1
        #         else:
        #             dct[j]=1
        # print(dct)
        # sorting = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
        # print(sorting)
        
        # return list(sorting)[0]
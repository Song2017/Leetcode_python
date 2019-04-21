class Solution:
    def twoCitySchedCost(self, costs) -> int:
        NA, NB = len(costs)//2, len(costs)//2
        rtn = 0
        A, B = [], []
        for cost in costs:
            A.append(cost[0])
            B.append(cost[1])
        while A:
            minA, minB = min(A), min(B)  
            # print(00, minA, minB)
            if minA < minB:
                if NA > 0: 
                    NA -= 1
                    rtn += minA
                    index = A.index(minA) 
                elif NB > 0:
                    NB -= 1
                    rtn += minB
                    index = B.index(minB) 
            else:
                if NB > 0: 
                    NB -= 1
                    rtn += minB
                    index = B.index(minB) 
                elif NA > 0:
                    NA -= 1
                    rtn += minA
                    index = A.index(minA)
            print(22, A, B, index,minA, minB, rtn, NA, NB)

            A.pop(index)
            B.pop(index)  
            #     print(1111, index)
        return rtn


s = Solution()
# print(s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))

#     1        2                       2      2
# [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
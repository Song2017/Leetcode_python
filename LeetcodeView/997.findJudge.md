class Solution:
    '''
    在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
    如果小镇的法官真的存在，那么：
        小镇的法官不相信任何人。
        每个人（除了小镇法官外）都信任小镇的法官。
        只有一个人同时满足属性 1 和属性 2 。
    给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
    如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1
    '''

    def findJudge0(self, N: int, trust) -> int:
        tf = []
        for tp in trust:
            tf.append(tp[0])

        tf = set(tf)
        if len(tf) != N - 1:
            return -1
        all = set()

        for i in range(1, N + 1):
            all.add(i)

        ans = list(all - tf)[0]
        tf = []
        for tp in trust:
            if tp[1] == ans:
                tf.append(tp[0])
        tf = set(tf)
        if len(tf) != N - 1:
            return -1
        return ans

    def findJudge(self, N: int, trust) -> int:
        '''
        用两个数组记录每个结点的入度和出度，出度(trusters)为0入度(trustees)为N的就是法官
        '''        
        if N < 2:
            return N
        trusters = [0] * (N + 1)
        trustees = [0] * (N + 1)
        for i, j in trust:
            trusters[j] += 1
            trustees[i] += 1
        max_cnt = max(trusters)
        # 每个人（除了小镇法官外）都信任小镇的法官, 只有一个法官
        if max_cnt != N - 1 or trusters.count(max_cnt) > 1:
            return -1
        cand = trusters.index(max_cnt)
        if trustees[cand] > 0:
            return -1
        return cand


s = Solution()
print(s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

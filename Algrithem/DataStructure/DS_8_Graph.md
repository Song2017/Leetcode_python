# 图 Graph 
图是一种非线性表结构, 用来模拟一组连接
图的算法有很多, 比如图的搜索、最短路径、最小生成树、二分图等
## 概念
    顶点（vertex）:图中的元素
    边（edge）:顶点之间建立的连接关系

    无向图: 边没有方向的图, 例如微信
    有向图: 边有方向的图, 例如微博
    带权图（weighted graph）:每条边都有一个权重（weight）. 带权图类比QQ, 权重就是QQ亲密度

    度（degree）: 与顶点相连接的边的条数, 比如微信中有多少好友
        有向图中根据边的指向分为: 入度（In-degree）和出度（Out-degree）

## 存储方式
### 邻接矩阵（Adjacency Matrix）
    邻接矩阵的底层依赖一个二维数组。
    对于无向图来说，如果顶点 i 与顶点 j 之间有边，我们就将 A[i][j] 和 A[j][i] 标记为 1；
    对于有向图来说，如果顶点 i 到顶点 j 之间，有一条箭头从顶点 i 指向顶点 j 的边，那我们就将 A[i][j] 标记为 1。同理，如果有一条箭头从顶点 j 指向顶点 i 的边，我们就将 A[j][i] 标记为 1。
    对于带权图，数组中就存储相应的权重
1. 缺点
    邻接矩阵来表示一个图，虽然简单、直观，但是当顶点多, 边比较少时比较浪费存储空间. 
2. 优点
    邻接矩阵的存储方式简单、直接，因为基于数组，所以在获取两个顶点的关系时，就非常高效。
    方便计算: Floyd-Warshall 算法, 直接计算邻接矩阵

### 邻接表存储方法（Adjacency List）
    每个顶点对应一条链表，链表中存储的是与这个顶点相连接的其他顶点
1. 缺点
    邻接表存储起来比较节省空间，但是使用起来就比较耗时间
2. 快速地查找两个顶点之间是否存在边    
我们可以将邻接表中的链表改成平衡二叉查找树。实际开发中，我们可以选择用红黑树。
当然，这里的二叉查找树可以换成其他动态数据结构，比如跳表、散列表等。
除此之外，我们还可以将链表改成有序动态数组，可以通过二分查找的方法来快速定位两个顶点之间否是存在边

## 图的应用 
### 广度优先搜索算法（BFS）
1. Breadth-First-Search: 是一种“地毯式”层层推进的搜索策略，即先查找离起始顶点最近的，
    然后是次近的，依次往外搜索
2. 广度优先搜索需要借助队列来实现，遍历得到的路径就是，起始顶点到终止顶点的最短路径
#### 二叉树层次遍历
```
class Solution:
    '''
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    '''
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        # q: 队列存储每层的节点
        ans, q = [], [root]
        while q:
            level, qt = [], []
            for n in q:
                level.append(n.val)
                # qt: 下一层节点的缓存, 要保持层内节点的顺序, 需要先添加左侧子节点
                if n.left:
                    qt.append(n.left)
                if n.right:
                    qt.append(n.right)
            q = qt
            ans.append(level)
        ans.reverse()
        return ans
```
### 深度优先搜索算法（DFS）
1. Depth-First-Search: 最直观的例子就是“走迷宫”
2. 深度优先搜索是借助栈来实现的, 用的是回溯思想，非常适合用递归实现
#### 全排列
```
class Solution:
    '''
    给定一个没有重复数字的序列，返回其所有可能的全排列
    '''
    def permute(self, nums):
        def dfs(first=0):
            if first == n:
                ans.append(nums.copy())
            for i in range(first, n):
                # split element with index i
                nums[first], nums[i] = nums[i], nums[first]
                # retrive all permute nums-nums[first]
                dfs(first + 1)
                # back track: restore nums
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        ans = []
        dfs()
        return ans
```

## Note 
### 算法图解示例
    在执行效率方面，深度优先和广度优先搜索的时间复杂度都是 O(E)，空间复杂度是 O(V)
    ```
    '''
    检查你的朋友中有没有芒果销售商
    使用散列表来实现图
    '''
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['alice'] = ['peggy']
    graph['bob'] = ['anuj', 'peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['jonny'] = []
    graph['thom'] = []
    graph['peggy'] = []
    mango_seller = ['thom']


    # bfs
    def search_mango_seller_nums(name):
        friends = graph[name]
        f_friends = []
        relation = 0
        while friends:
            relation += 1
            for person in friends:
                if person in mango_seller:
                    return relation
                else:
                    f_friends += graph[person]
            friends = f_friends
        return relation


    print(search_mango_seller_nums('you'))

    # add mango seller
    graph['you'] = ['alice', 'bob', 'claire', 'tom']
    mango_seller = ['thom', 'tom']
    graph['tom'] = ['suny']


    # dfs: get all path from you to mango seller
    def search_mango_seller_relations(name):
        relation = []
        ans = []

        def dfs(name):
            # add friends who are going to be searched
            relation.append(name)
            if name in mango_seller:
                ans.append(relation.copy())
            else:
                for person in graph[name]:
                    dfs(person)
            # reset friends for next search
            relation.pop()

        dfs(name)
        return ans


    print(search_mango_seller_relations('you'))
    ```
### N皇后的三种解法
    ```
    class Solution:
        def solveNQueens(self, n: int):
            '''
            n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
            二维矩阵存储棋盘状态, 采用递归解法
            '''

            def dfs(row, board, ret, size):
                # print(board, size, row)
                if row == size:
                    ret.append(["".join(i) for i in board])
                    return
                # 对每一列进行尝试
                for i in range(size):
                    if not canPlace(row, i, board, size):
                        continue
                    board[row][i] = 'Q'
                    # 对每一行进行尝试, 同时也是回溯点
                    dfs(row + 1, board, ret, size)
                    # !! 将棋盘恢复为未摆放的状态
                    board[row][i] = '.'

            def canPlace(row, col, board, size):
                # 只要对判断行之上的行进行判断, 当前判断行将要放置, 也不需要判断
                for i in range(1, row + 1):
                    # 同一列
                    if board[row - i][col] == 'Q':
                        return False
                    # 上半对角线
                    if col - i >= 0 and board[row - i][col - i] == 'Q':
                        return False
                    # 上半逆对角线
                    if col + i < size and board[row - i][col + i] == 'Q':
                        return False

                return True

            board, ret = [['.'] * n for _ in range(n)], []
            dfs(0, board, ret, n)
            return ret

        def solveNQueensOneDim(self, n: int):
            '''
            一维矩阵存储棋盘状态, 采用递归解法
            判断是否可以放置的条件:
                1, 判断列, 2, 判断两斜线: 行和列到将要放置点的距离相等的点是否已被放置
            '''
            memo, ret = [0] * n, []

            def canPlace(row, col):
                for i in range(0, row):
                    if memo[i] == col or abs(col - memo[i]) == abs(row - i):
                        return False
                return True

            def dfs(row):
                if row == n:
                    graph = []
                    for i in memo:
                        graph.append('.' * i + 'Q' + '.' * (n - i - 1))
                    ret.append(graph)
                    return
                for i in range(n):
                    if not canPlace(row, i):
                        continue
                    memo[row] = i
                    dfs(row + 1)
                    memo[row] = 0

            dfs(0)
            return ret

        def solveNQueensRe(self, n: int):
            '''
            一维矩阵存储棋盘状态, 采用迭代
            '''
            memo, row, ret, graph = [0] * (n + 1), 1, [], []

            def canPlace(col):
                for i in range(1, col):
                    # 判断列, 判断两斜线: 行和列到当前点的距离相等的位置
                    if memo[i] == memo[col] or abs(memo[col] -
                                                memo[i]) == abs(col - i):
                        return False
                return True

            # 从第1行开始, 索引为0的行作为退出条件
            while row > 0:
                memo[row] += 1
                # 当前行放置, 不能放则
                while memo[row] <= n and not canPlace(row):
                    memo[row] += 1
                if memo[row] <= n:
                    # 已经放到最后一行了
                    if row == n:
                        graph = []
                        for i in memo[1:]:
                            graph.append('.' * (i - 1) + 'Q' + '.' * (n - i))
                        ret.append(graph)
                    else:
                        # 判断下一行
                        row += 1
                        # 下一行从第0列开始判断
                        memo[row] = 0
                else:
                    row -= 1
            return ret


    s = Solution()
    print(s.solveNQueensRe(11))

    ```
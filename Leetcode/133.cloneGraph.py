# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    '''
    给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。
    图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）    
    '''

    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        广度优先搜索 + 散列表
        广度优先搜索: 逐层(节点->邻居节点)复制数据
        散列表: 记录原node 和 新node的对应关系
        '''
        ans = {node: Node(node.val, [])}
        root = [node]
        while root:
            queue = []
            # root 层
            for o_root in root:
                n_root = ans.get(o_root)
                # neighbor 层
                for o_node in o_root.neighbors:
                    n_node = ans.get(o_node)
                    if n_node:
                        # 新node已经创建, 添加建立连接后直接返回
                        n_root.neighbors.append(n_node)
                        continue
                    n_node = Node(o_node.val, [])
                    ans[o_node] = n_node
                    n_root.neighbors.append(n_node)
                    queue.append(o_node)
            root = queue

        return ans[node]

    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        '''
        深度优先搜索 + 散列表
        深度优先搜索: 使用队列缓存需要创建新节点的原节点
        散列表: 记录原node 和 新node的对应关系
        '''
        # {原来的节点: 复制后的节点}
        ans = {node: Node(node.val, [])}
        # 原来的节点
        queue = [node]
        while queue:
            current = queue.pop(0)
            for neis in current.neighbors:
                if neis not in ans:
                    ans[neis] = Node(neis.val, [])
                    queue.append(neis)
                # 复制后的节点建立连接
                ans[current].neighbors.append(ans[neis])
        return ans[node]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    '''
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
    同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
    你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。    
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        bfs: 层序遍历, 队列, 先进先出
        """
        ans = ""
        if not root:
            return ans
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop(0)
            if cur is None:
                ans += "null,"
                continue
            ans += str(cur.val) + ","
            stack.append(cur.left)
            stack.append(cur.right)
        return ans.rstrip(',')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        队列: 存储每层的树节点
        """
        if not data:
            return None
        nodes = data.split(',')
        queue = []
        head = cur = TreeNode(nodes.pop(0))
        queue.append(cur)
        while queue:
            cur = queue.pop(0)
            val = nodes.pop(0)
            if val == 'null':
                cur.left = None
            else:
                cur.left = TreeNode(val)
                queue.append(cur.left)
            val = nodes.pop(0)
            if val == 'null':
                cur.right = None
            else:
                cur.right = TreeNode(val)
                queue.append(cur.right)
        return head


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

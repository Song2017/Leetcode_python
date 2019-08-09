
# Tree 树
树是一种非线性数据结构,它是由n(n>=1)个有限结点组成一个具有层次关系的集合.
## 概念
1. 节点: 组成树的元素
为了更好的描述节点间的关系, 对节点间的关系进行了定义.
    
	    父节点,子节点,兄弟节点
	    根节点,叶节点
2. Height, Depth, Level

		节点的高度: 节点到叶节点的最长边数, 从下向上度量 叶节点高度为0
		节点的深度: 根节点到此节点的边数, 从上向下度量 根节点深度为0
		节点的层数: 节点的深度 + 1
		树的高度: 根节点的高度

## 二叉树
每个节点至多有两个子节点的树, 称之为左子节点和右子节点
二叉树是最常用的, 当然根据子节点的最大个数, 还可以分为四叉, 八叉...
### 二叉树的存储
1. 基于指针的二叉链式存储法
```
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
```
2. 基于数组的顺序存储法
节点X存储在数组中下标为i的位置,下标为2 * i 的位置存储的就是左子节点,下标为 2 * i+1的位置存储的就是右子节点.
反过来,下标为 i/2 的位置存储就是它的父节点.
通过这种方式,我们只要知道根节点存储的位置(一般情况下,为了方便计算子节点,根节点会存储在下标为 1 的位置)

### 二叉树的分类
为了更好的使用二叉树解决查询,排序等操作, 根据常用的结构对二叉树进行分类

	1. 满二叉树: 除叶节点外, 每个节点都有两个子节点. 每层的节点数目: 1,2,4,8..
	2. 完全二叉树: 叶子节点都在最底下两层,最后一层的叶子节点都靠左排列,
	    并且除了最后一层,其他层的节点个数都要达到最大.
	    1. 直观的, 满二叉树是一种特殊的完全二叉树
	    2. 为什么最后一层的页节点要靠左排列? 
	        基于数组的顺序存储时, 靠左排列可以更好的节省内存
	    3. 堆: 完全二叉树 + 降低要求后的二叉搜索树
	    4. 从树的高度(形态)进行了限制
	    
	3. 二叉查找树(二叉搜索树): 任意一个节点,其左子树中的每个节点的值,都要小于这个节点的值,
	    而右子树节点的值都大于这个节点的值
	    1. 中序遍历的二叉查找树的结果是有序的
	    2. 树的高度没有限制, 时间复杂度跟O(Height)成正比
	    3. 从节点的数据(内容)进行了限制
	4. 平衡二叉查找树: 二叉树中任意一个节点的左右子树的高度相差不能大于 1
	    1. 兼具完全二叉树和二叉查找树的特性, 是一种限制了高度的二叉查找树

### 二叉树的遍历
![](https://img-blog.csdnimg.cn/20190327204247997.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NnczU5NTU5NQ==,size_16,color_FFFFFF,t_70)
分类的标准是节点与它的左右子树节点遍历打印的先后顺序(参考上图):
数字表示数组索引
	
	前序遍历: 先打印这个节点,然后再打印它的左子树,最后打印它的右子树
	    A-> B-> D-> H-> I-> E-> C-> F-> G
	中序遍历: 先打印它的左子树,然后再打印它本身,最后打印它的右子树
	    画图法: 将每层的节点垂直的落到底层上就是遍历的结果   
	    H-> D-> I-> B-> E-> A-> F-> C-> G
	后序遍历: 先打印它的左子树,然后再打印它的右子树,最后打印这个节点本身
	    H-> I-> D-> E-> B-> F-> G-> C-> A
	层序遍历: 按层遍历, 借用队列辅助,根节点先入队列,
	    然后循环从队列中pop节点,将pop出来的节点的左子节点先入队列,右节点后入队列,
	    依次循环,直到队列为空,遍历结束

#### 遍历的实现
1. 前序遍历
```
    preOrder(r) = print r->preOrder(r->left)->preOrder(r->right)
    def preorderTraversal(self, root: TreeNode):
        if root is None:
            return []
        rtn, stack = [], [root]
        while stack:
            root = stack.pop()
            rtn.append(root)
            # pop: 先弹出后入的元素
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return rtn
```
2. 中序遍历
```
    inOrder(r) = inOrder(r->left)->print r->inOrder(r->right)
    def inorderTraversal(self, root: TreeNode):    
    rtn, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            rtn.append(root.val)
            root = root.right 
```
3. 后序遍历
```
    postOrder(r) = postOrder(r->left)->postOrder(r->right)->print r
    def postorderTraversalF(self, root):
        """ 
        后序遍历: 左右根
        入栈: 左右
        出栈: 根右左
        结果: 取反
        """
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        return output[::-1]
```
#### 时间复杂度
根据递推公式, 每个子节点要访问节点一次, 也就是说节点最多被访问两次, O(n)

## 二叉查找树
### 是什么
任意一个节点,其左子树中的每个节点的值,都要小于这个节点的值,
    而右子树节点的值都大于这个节点的值
### 重要特性
中序遍历二叉查找树,可以输出有序的数据序列,时间复杂度是 O(n).
因此,二叉查找树也叫作二叉排序树
### 查找操作
	1. 先取根节点,如果它等于我们要查找的数据,那就返回.
	    如果要查找的数据比根节点的值小,那就在左子树中递归查找
	    如果要查找的数据比根节点的值大,那就在右子树中递归查找
	2. 代码实现
```
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        elif val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
```    
### 插入操作
	1. 新插入的数据一般都是在叶子节点上,所以我们只需要从根节点开始,依次比较要插入的数据和节点的大小关系
	    如果要插入的数据比节点的数据大,并且节点的右子树为空,就将新数据直接插到右子节点的位置;
	    如果不为空,就再递归遍历右子树,查找插入位置.
	    同理,如果要插入的数据比节点数值小,并且节点的左子树为空,就将新数据插入到左子节点的位置;
	    如果不为空,就再递归遍历左子树,查找插入位置
    2. 代码实现
```
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)    
        if root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            new = TreeNode(val)
            new.right = root.right
            root.right = new
        return root
```
### 删除操作
	1. 针对要删除节点的子节点个数的不同,我们需要分三种情况来处理 
	    1. 如果要删除的节点没有子节点,我们只需要直接将父节点中,指向要删除节点的指针置为 null.
	    2. 如果要删除的节点只有一个子节点(只有左子节点或者右子节点),
	    我们只需要更新父节点中,指向要删除节点的指针,让它指向要删除节点的子节点就可以了.
	    3. 如果要删除的节点有两个子节点, 
	    我们需要找到这个节点的右子树中的最小节点,把它替换到要删除的节点上.
	    然后再删除掉这个最小节点,因为最小节点肯定没有左子节点(如果有左子结点,那就不是最小节点了)
2. 代码实现
```
 def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
                
        parent = None
        node = root
        while (node and node.val != key):
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right
        # not found
        if not node:
            return root
        # node does't has child
        elif not node.left and not node.right:
            # not root
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return root
            # root
            return None
        # node  has two children
        elif node.left and node.right:
            pre_parent = node
            pre = node.left
            while pre.right:
                pre_parent = pre
                pre = pre.right
            if pre_parent != node:
                pre_parent.right = pre.left
                node.val = pre.val
            else:
                node.val = pre.val
                node.left = pre.left
            return root           
        
        # node only has one child
        else:
            if parent:
                if parent.left == node:
                    parent.left = node.left or node.right
                else:
                    parent.right = node.left or node.right
                return root
            else:
                return node.left or node.right
```
### 其他操作
	1. 快速地查找最大节点和最小节点,前驱节点和后继节点
	2. 二叉查找树中存储对象,我们利用对象的某个字段作为键值(key)来构建二叉查找树
	    卫星数据:对象中的其他字段
	3. 存储的两个值相同的情况
	    1. 通过链表和支持动态扩容的数组等数据结构,把值相同的数据都存储在同一个节点
	    2. 每个节点仍然只存储一个数据.
	        1. 插入数据,我们就将这个要插入的数据放到这个相同的值的节点的右子树,
	        也就是说,把这个新插入的数据当作大于这个节点的值来处理
	        2. 查找数据的时候,遇到值相同的节点,我们并不停止查找操作,
	        而是继续在右子树中查找,直到遇到叶子节点,才停止
	        3. 删除操作,我们也需要先查找到每个要删除的节点,然后再按前面讲的删除操作的方法,依次删除
### 时间复杂度
	二叉查找树没有对树的高度进行限制(完全二叉树: 不限制顺序, 但限制高度), 这就导致二叉查找树的形态很多.
	根节点的左右子树极度不平衡时,退化成了链表.
	不限制高度的二叉查找树时间复杂度近似的跟树的高度成正比,也就是 O(height).
	为了提高效率, 可以添加完全二叉树条件限制高度, 这就是平衡二叉查找树
	下面求完全二叉树的时间复杂度, 结合完全二叉树定义及等比求和公式
	设层数为L, 且每层的数目为2^(L-1), 因为最后一层根节点数目为[1, 2^(L-1)]
	    倒数第二层: n >= 1+2+4+8+...+2^(L-2)+1 = 2^(L-1)
	    底层为满: n <= 1+2+4+8+...+2^(L-2)+2^(L-1) = 2^L-1
	得到: L 的范围是 [log2(n+1), log2n +1]

## 红黑树 RB-Tree
### 平衡二叉查找树: 
	1. 严格的定义: 二叉树中任意一个节点的左右子树的高度相差不能大于 1
	2. 为了解决二叉查找树在频繁的插入,删除等动态更新的情况下,出现时间复杂度退化的问题, 发明了平衡二叉查找树.
	    “平衡”的意思,其实就是让整棵树左右看起来比较“对称”,不要出现左,右子树高度相差很大的情况,
	    相应的插入,删除,查找等操作的效率高一些
	3. 兼具 完全二叉树和二叉查找树的特性, 是一种限制了高度的二叉查找树
	3. 分类包括AVL树, Splay Tree(伸展树),Treap(树堆)等, 红黑树也是一种平衡二叉查找树 
### 红黑树 
	1. 是一种不严格的平衡二叉查找树, 也就是性能不会退化的太严重.
	2. 定义:
	    1. 红黑树的节点,一类被标记为黑色,一类被标记为红色,根节点是黑色的;
	    2. 每个叶子节点都是黑色的空节点(NIL),也就是说,叶子节点不存储数据,主要是为了简化红黑树的代码实现;
	    3. 任何相邻的节点都不能同时为红色,也就是说,红色节点是被黑色节点隔开的;
	    4. 每个节点,从该节点到达其可达叶子节点的所有路径,都包含相同数目的黑色节点;
	        如果去掉红节点, 就变成了完全多叉树,数的高度小于log2n. 子树的高度完全一致, 只是子节点数目会变多
	3. 时间复杂度
	    每个节点到达叶子节点的所有路径,都包含相同数目的黑色节点, 所以子树的高度会完全一致, 
	    也就是说去掉红节点后, 黑树的高度不会超过log2n, 
	    又因为红色节点是被黑色节点隔开, 所以加入红色节点之后,最长路径不会超过 2log2n
	4. AVL 树 VS 红黑树
	AVL 树是一种高度平衡的二叉树,所以查找的效率非常高,
	但是,AVL 树为了维持这种高度的平衡,每次插入,删除都要做调整,就比较复杂,耗时.
	所以,对于有频繁的插入,删除操作的数据集合,使用 AVL 树的代价就有点高了.
	红黑树只是做到了近似平衡,并不是严格的平衡,所以在维护平衡的成本上,要比 AVL 树要低
### 实现红黑树
#### 基本思想
红黑树的平衡过程跟魔方复原非常神似,大致过程就是：遇到什么样的节点排布,我们就对应怎么去调整
#### 实现 TBC...
1. 左旋(rotate left), 全称叫围绕某个节点的左旋
    右旋(rotate right),叫围绕某个节点的右旋

## Note
	1. 给定一组数据,比如 1,3,5,6,9,10.你来算算,可以构建出多少种不同的二叉树
	    [卡特兰数](https://en.wikipedia.org/wiki/Catalan_number) * 排列(无重复值时n!)
	    Catalon number: f(n) = f(k) * f(n-k-1),k: 0... n - 1 
	                    f(n) = f(0)f(n-1) + ... + f(n-1)f(0) 
	2. 散列表 VS 平衡二叉查找树
	    散列表: 插入,删除,查找操作的时间复杂度可以做到常量级的 O(1) 
	    平衡二叉查找树: 插入,删除,查找操作时间复杂度是O(logn)
	为什么还要用二叉查找树呢?
	    1. 有序性, 散列表中的数据是无序存储的,如果要输出有序的数据,需要先进行排序.而对于二叉查找树来说,我们只需要中序遍历,就可以在 O(n) 的时间复杂度内,输出有序的数据序列.
	    2. 稳定性, 散列表扩容耗时很多,而且当遇到散列冲突时,性能不稳定,但是平衡二叉查找树的性能非常稳定,时间复杂度稳定在 O(logn).
	    3. 耗时, 尽管散列表的查找等操作的时间复杂度是常量级的,但因为哈希冲突的存在,这个常量不一定比logn 小,所以实际的查找速度可能不一定比O(logn)快.加上哈希函数的耗时,也不一定就比平衡二叉查找树的效率高.
	    4. 复杂度, 散列表的构造比二叉查找树要复杂,需要考虑的东西很多.比如散列函数的设计,冲突解决办法,扩容,缩容等.平衡二叉查找树只需要考虑平衡性这一个问题,而且这个问题的解决方案比较成熟,固定.
	    5. 内存空间, 为了避免过多的散列冲突,散列表装载因子不能太大,特别是基于开放寻址法解决冲突的散列表,不然会浪费一定的存储空间
	只需要插入,查找操作时使用散列表, 一旦牵扯到排序使用平衡二叉树. 有性能及内存空间要求时, 尽可能多的使用平衡二叉树

class Solution:
    '''
    编写一个函数来查找字符串数组中的最长公共前缀。
    1、所求的最长公共前缀子串一定是每个字符串的前缀子串。所以随便选择一个字符串作为标准，
    把它的前缀串，与其他所有字符串进行判断，看是否是它们所有人的前缀子串。这里的时间性能是O(m*n*m)。
    2、列出所有的字符串的前缀子串，将它们合并后排序，找出其中个数为n且最长的子串。
    时间性能为O(n*m+m*n*log(m*n))
    3、纵向扫描：从下标0开始，判断每一个字符串的下标0，判断是否全部相同。
    直到遇到不全部相同的下标。时间性能为O(n*m)。
    4、横向扫描：前两个字符串找公共子串，将其结果和第三个字符串找公共子串……直到最后一个串。
    时间性能为O(n*m)。
    5、借助trie字典树。将这些字符串存储到trie树中。那么trie树的第一个分叉口之前的单分支树的就是所求
    '''

    def __init__(self):
        self.trie = {}
        self.end = '$'

    def trieInsert(self, word):
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.end] = self.end

    def longestCommonPrefix(self, strs) -> str:
        ans = ''
        for w in strs:
            self.trieInsert(w)
        trie = self.trie
        while self.end not in trie.keys() and len(trie.keys()) == 1:
            key = next(iter(trie))
            ans += key
            trie = trie[key]
        return ans

    def longestCommonPrefixF(self, strs):
        '''
        利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，
        然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
        '''
        if not strs:
            return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for x in ss:
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


s = Solution()
# print(s.longestCommonPrefixF(["flower", "flow", "flight"]))
# print(s.longestCommonPrefixF(["", "b"]))
# print(s.longestCommonPrefix(["aa", "a"]))
print(s.longestCommonPrefix(["a", 'a', '']))
# print(s.longestCommonPrefix(["dog", "dracecar", "dcar"]))

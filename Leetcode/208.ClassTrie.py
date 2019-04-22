class TrieNode:
    def __init__(self):
        self._is_end = False
        self._child = [None] * 26


class Trie:
    '''
    构建26叉树
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self._root
        for i in map(lambda x: ord(x) - ord('a'), word):
            if not node._child[i]:
                node._child[i] = TrieNode()
            node = node._child[i]
        node._is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._root
        for i in map(lambda x: ord(x) - ord('a'), word):
            if not node._child[i]:
                return False
            node = node._child[i]
        return node._is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given 
            prefix.
        """
        node = self._root
        for i in map(lambda x: ord(x) - ord('a'), prefix):
            if not node._child[i]:
                return False
            node = node._child[i]
        return True


class TrieFast:
    '''
    字典结构缓存字符串的纵向字符列
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.flag = '#'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for each in word:
            if each not in node:
                node[each] = {}
            node = node[each]
        node[self.flag] = self.flag

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for each in word:
            if each not in node:
                return False
            node = node[each]
        return self.flag in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given 
            prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for each in prefix:
            if each not in node:
                return False
            node = node[each]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
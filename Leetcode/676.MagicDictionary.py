class MagicDictionary:
    '''
    实现一个带有buildDict, 以及 search方法的魔法字典。
    对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。
    对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，
    使得所形成的新单词存在于你构建的字典中
    字符量少时, 按子符长度分组, 原生字符直接添加到分组中, 分别校验每组里的字符;
    字符量很大时, 对字符求hash值, 分组后往里添加hash值, 计算并比较26*len(word)次hash值后得到结果
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.len_words = defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.len_words[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word 
        after modifying exactly one character
        """
        n = len(word)
        for w in self.len_words[n]:
            d = 0
            for i in range(n):
                if w[i] != word[i]:
                    d += 1
            if d == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
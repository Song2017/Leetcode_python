class MagicDictionary:
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
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
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
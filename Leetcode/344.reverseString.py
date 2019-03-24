class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) == 0:
            return None
        al = len(s) - 1
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[al - i]
            s[al - i] = tmp
        return None

    def reverseStringBuiltIn(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]

    def reverseStringFast(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        前后两两交换+python的快照特性
        """
        l, u = 0, len(s) - 1
        while l <= u:
            s[l], s[u] = s[u], s[l]
            l, u = l + 1, u - 1
        return None


s = Solution()
print(s.reverseStringFast(["h", "e", "l", "l", "o", '1']))
print(s.reverseStringFast(["h", "e", "l", "l", "o"]))

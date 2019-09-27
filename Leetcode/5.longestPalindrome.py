class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        https://www.felix021.com/blog/read.php?2040
        Manacher's ALGORITHM: O(n)时间求字符串的最长回文子串
        马拉车算法很好的利用已知回文子串,center 为已知的 右边界最大 的回文子串的中心
        当i是center为中心回文串的一个节点时, 那么i关于center就是对称的
        """
        # 偶数的回文的中心可以处于两字母之间, 判断逻辑不同, 统一转成奇数
        separator, s2, r_border, center = '#', '#', 0, 0
        for c in s:
            s2 = s2 + c + separator
        n = len(s2)
        p = [0] * n

        for i in range(1, n):
            # 设center 为已知的 右边界最大 的回文子串的中心，i为循环的节点
            # p[i] 表示以i为中心的回文串的半径长度
            # r_border 表示子串的右边界, 则为 center+P[center]
            # i可能是以center为中心回文串的一个节点, 那么i关于center就是对称的
            # i关于center的对称点可以表示为 center-(i-center) = center * 2 - i]
            p[i] = min(p[center * 2 - i], r_border - i) if r_border > i else 1
            # 计算i位置的回文串单边长度
            while i + p[i] < n and s2[i - p[i]] == s2[i + p[i]]:
                p[i] += 1
            # 新的回文串单边长度大于已存在的
            if p[i] > r_border - i:
                center, r_border = i, i + p[i]
        max_p = max(p)
        m_center = [i for i, v in enumerate(p) if v == max_p][-1]
        return s2[m_center - max_p + 1:m_center + max_p].replace(separator, '')

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        时间 O(n**2), 空间O(1)
        可以每次循环选择一个中心，进行左右扩展，判断左右字符是否相等
        """
        length = len(s)
        if length < 2 or s == s[::-1]:
            return s
        max_len, begin = 1, 0
        for i in range(1, length):
            odd = s[i - max_len - 1:i + 1]
            even = s[i - max_len:i + 1]
            # 回文串是奇数:回文中心是一个字符, 中心位置比最大长度至少大于1
            # 最大长度一次多俩字符
            if i - max_len >= 1 and odd == odd[::-1]:
                begin = i - max_len - 1
                max_len += 2
                continue
            # 回文串是奇数:回文中心是一个字符, 回文串是对称的
            if i - max_len >= 0 and even == even[::-1]:
                begin = i - max_len
                max_len += 1
        return s[begin:begin + max_len]


if __name__ == "__main__":
    Solution1 = Solution()
    print(Solution1.longestPalindrome("abcbadd"))

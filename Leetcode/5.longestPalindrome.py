class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        https://www.felix021.com/blog/read.php?2040
        Manacher's ALGORITHM: O(n)时间求字符串的最长回文子串  不指定
        """
        sc, si, mx, id = '#', '#', 0, 0
        for c in s:
            si = si + c + sc
        n = len(si)
        p = [0] * n

        for i, c in enumerate(si):
            if i == 0:
                continue
            # id 为已知的 {右边界最大} 的回文子串的中心，
            # mx则为id+P[id]，也就是这个子串的右边界
            # j = 2 * id - i，也就是说 j 是 i 关于 id 的对称点(j = id - (i - id))
            p[i] = min(p[id * 2 - i], mx - i) if mx > i else 1
            # 计算i位置的回文串单边长度
            while i + p[i] < n and si[i - p[i]] == si[i + p[i]]:
                p[i] += 1
            # 新的回文串单边长度大于已存在的
            if p[i] > mx - i:
                id, mx = i, i + p[i]
        mxp = max(p)
        cindex = [i for i, v in enumerate(p) if v == mxp][-1]
        return si[cindex - mxp + 1:cindex + mxp].replace(sc, '')

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2 or s == s[::-1]: return s
        max_len, begin = 1, 0
        for i in range(1, length):
            odd = s[i - max_len - 1:i + 1]
            even = s[i - max_len:i + 1]
            if i - max_len >= 1 and odd == odd[::-1]:
                begin = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                begin = i - max_len
                max_len += 1
        return s[begin:begin + max_len]


Solution1 = Solution()
print(Solution1.longestPalindrome("abcba"))
print(Solution1.longestPalindrome("aaaa"))
print(Solution1.longestPalindrome("babad"))
print(Solution1.longestPalindrome("bb"))
print(Solution1.longestPalindrome("121"))
print(Solution1.longestPalindrome("cbbd"))
print(Solution1.longestPalindrome("a"))
print(Solution1.longestPalindrome("ac"))

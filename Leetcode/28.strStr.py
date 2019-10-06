class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP: 优化了匹配公共子前缀的时间
        KMP 里的一个重要数据结构——最长的公共前缀和后缀，英文是 Longest Prefix and Suffix，简称 LPS。
        LPS 其实是一个数组，记录了字符串从头开始到某个位置结束的一段字符串当中，公共前缀和后缀的最大长度。
        所谓公共前缀和后缀，就是说字符串的前缀等于后缀，并且，前缀和后缀不能是同一段字符串
        ABCDAB 的 LPS 为 2，即，对于 ABCDAB ，它最后两个字符一定与它最前面两个字符相等      
        """
        nh = len(haystack)
        nn = len(needle)
        if nn == 0:
            return 0
        if nn > nh:
            return -1            
        # get LPS
        def getLPS(s):
            i, cnt = 1, 0
            lps = [0] * nn
            while i < nn:
                if s[i] == s[cnt]:
                    cnt += 1
                    lps[i] = cnt
                    i += 1
                elif cnt > 0:
                    cnt -= 1
                else:
                    i += 1
            return lps

        lps = getLPS(needle)
        # print(lps)
        i, j = 0, 0
        # compare
        while i < nh:
            if haystack[i] == needle[j]:
                if j == nn - 1:
                    return i - nn + 1
                i += 1
                j += 1
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1

        return -1


if __name__ == "__main__":
    s = Solution()
    # print(s.strStr("hlello", "ll"))
    print(s.strStr("abc abcdab ddabcdabdasda", "abcdabd"))


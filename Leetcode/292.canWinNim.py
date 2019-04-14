class Solution:
    def canWinNim(self, n: int) -> bool:
        # 巴适博弈
        # https://blog.csdn.net/Lionel_D/article/details/43939605
        return n % 4 != 0
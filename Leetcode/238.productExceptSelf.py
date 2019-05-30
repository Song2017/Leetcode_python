class Solution:
    def productExceptSelf(self, nums):
        '''
        存在2个及以上的0, 结果都是0
        有一个0, 则非0元素都是0
        不含0时, 所有的乘积除以元素自身的值
        '''
        cnt = 0
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
                index = i     
        if cnt > 1:
            for i in range(n):
                nums[i] = 0
        elif cnt == 1:
            nums[index] = 1
            for j in range(n):
                if j == index:
                    continue
                nums[index] *= nums[j]
                nums[j] = 0
        else:
            s = 1
            for i in nums:
                s *= i
            for i in range(n):
                nums[i] = s // nums[i]
        return nums

    def productExceptSelfF(self, nums):
        '''
        分两步进行相乘: 1, 先对指定元素以前的元素求积, 缓存到返回数组;
                    2, 对第一步逆向执行, 求指定元素后面的元素的积, 然后乘上缓存的值, 得到结果
        '''
        tmp = 1
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(tmp)
            tmp *= nums[i]
        tmp = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= tmp
            tmp *= nums[i]
        return ans


s = Solution()
print(s.productExceptSelf([0, 2, 0]))

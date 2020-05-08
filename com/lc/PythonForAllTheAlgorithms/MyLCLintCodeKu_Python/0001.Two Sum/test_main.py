from Solution import Solution

# 这个使用from Solution import Solution引入
# main方法
if __name__ == '__main__':
    slt = Solution()
    target = 10
    nums = [1, 2, 8, 5]
    temp = slt.twoSum(nums, target)
    print(temp)

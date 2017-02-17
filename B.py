# coding=utf-8

nums = [1, 2, 3, 5, 7, 11]


def minimum_difference(nums):
    n = len(nums)
    nums_sum = sum(nums)
    tar = nums_sum / 2
    dp = [[0] * (tar+1)] * (n+1)
    nums = [0] + nums

    for i in xrange(1, n+1):
        for j in xrange(1, tar+1):
            if j < nums[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
    return nums_sum - 2 * dp[n-1][tar]


if __name__ == '__main__':
    print 'min diff is', minimum_difference(nums)

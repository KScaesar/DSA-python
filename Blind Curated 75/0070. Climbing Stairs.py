class Solution:
    # https://leetcode.com/problems/climbing-stairs/

    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 1)
        case_1 = 1
        case_2 = 2

        dp_n = -1
        prev_1 = -1
        prev_2 = -1

        for i in range(1, n + 1):
            if i == 1:
                dp_n = case_1
                prev_2 = case_1
            elif i == 2:
                dp_n = case_2
                prev_1 = case_2
            else:
                dp_n = prev_1 + prev_2  # dp[i] = dp[i - 1] + dp[i - 2]
                prev_2 = prev_1
                prev_1 = dp_n

        return dp_n


if __name__ == '__main__':
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))

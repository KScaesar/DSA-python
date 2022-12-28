class Solution:
    # https://leetcode.com/problems/number-of-1-bits/
    def hammingWeight(self, n: int) -> int:
        ans = 0
        i = 0
        while n:
            flag = 1 << i
            if n & flag:
                ans += 1
                n = n ^ flag
            i += 1
        return ans


if __name__ == '__main__':
    print(Solution().hammingWeight(0b00000000000000000000000000001011))

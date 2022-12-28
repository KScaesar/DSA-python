class Solution:
    # https://leetcode.com/problems/reverse-bits/description/
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            flag = 1 << i
            if n & flag:
                ans |= 1 << (31 - i)
        return ans


if __name__ == '__main__':
    print(Solution().reverseBits(0b00000010100101000001111010011100))
    # print(len('00000010100101000001111010011100'))

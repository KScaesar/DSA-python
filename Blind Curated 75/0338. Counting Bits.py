from typing import List


class Solution:
    # https://leetcode.com/problems/counting-bits/
    def countBits_v2(self, n: int) -> List[int]:
        # O(N)

        # 寫法1
        # https://github.com/halfrost/LeetCode-Go/tree/master/leetcode/0338.Counting-Bits

        # 寫法2
        # 觀察數字規律
        # https://github.com/aQuaYi/LeetCode-in-Go/blob/master/Algorithms/0338.counting-bits/counting-bits.go
        # https://leetcode.com/problems/counting-bits/solutions/79539/three-line-java-solution/?orderBy=most_votes

        # i >> 1 == i/2
        # i & 1  == i%2
        # X&1 判断奇偶性，X&1>0 即奇数
        # X = X & (X-1) 清零最低位的1

        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1

        return ans

    def countBits_v1(self, n: int) -> List[int]:
        # N*logN
        # 雖然題目說很容易想到 N*logN 的解法
        # 但我第一時間想不到, 該怎麼作

        ans = [0] * (n + 1)
        for i in range(n + 1):
            v = i
            while v:
                if v & 1:
                    ans[i] += 1
                v = v >> 1

        return ans


if __name__ == '__main__':
    print("expect = [0,1,1,2,1,2]", Solution().countBits_v1(5))
    print("expect = [0,1,1,2,1,2]", Solution().countBits_v2(5))

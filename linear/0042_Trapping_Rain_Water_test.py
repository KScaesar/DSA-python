from typing import List


# https://leetcode.com/problems/trapping-rain-water/
# https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/ru-he-gao--0d5eb/
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size <= 2:
            return 0

        # 類似 memo 的功能
        l_max = [0] * size  # 當 cursor=i, left height [l~i] 之間的最大值
        r_max = [0] * size  # 當 cursor=i, right height [i~r] 之間的最大值
        for i in range(size):
            l_max[i] = max(height[:i + 1])  # 要把自己也包含進去
            r_max[i] = max(height[i:size])  # 要把自己也包含進去

        ans = 0
        for i in range(1, size):
            ans += min(l_max[i], r_max[i]) - height[i]

        print("\n", height)
        return ans

    def trap_two_pointer(self, height: List[int]) -> int:
        # 解題策略:一格一格判斷能不能裝水
        # 每格子更新時所需做的判斷:
        # 1. 左右兩邊牆誰比較矮
        # 2. 當下 Index 格子跟矮牆誰比較高
        #       a.index : 更新牆壁高度
        #       b.牆: 裝水
        # 3. 決定下一個 Index 是左 Pointer 還是右 Pointer
        # 4. 移動 Pointer 後重複循環
        pass


def test_trap_success():
    testcase = [
        (
            ([4, 2, 0, 3, 2, 5],),
            9,
        )
    ]

    for param, expected in testcase:
        assert Solution().trap(*param) == expected

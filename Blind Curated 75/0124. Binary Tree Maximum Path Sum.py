from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/

    # 重點題目, 多加複習, 前序 後序 的意義
    def maxPathSum_v1(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/

        ans = float('-inf')

        def oneSideMaxSum(root) -> int:
            nonlocal ans

            if root is None:
                return 0

            # 利用 max 排除 負號的情況
            left = max(oneSideMaxSum(root.left), 0)
            right = max(oneSideMaxSum(root.right), 0)

            # 和 v1_fail 仔細比較, 想法差異在哪邊
            ans = max(ans, left + root.val + right)

            return max(left, right) + root.val

        oneSideMaxSum(root)
        return int(ans)

    def maxPathSum_v1_fail(self, root: Optional[TreeNode]) -> int:
        # https://labuladong.github.io/algo/2/21/36/
        # 使用後序的想法是這正確的, 因為這樣才可以拿到 左右子樹的資訊
        # 但是原題目的函數定義, 會造成 左右互相影響
        #
        # 因此重新定義一個不會互相影響的函數, 只求單邊的最大距離是多少, 只能一直往下, 不能轉彎
        # 類似於 求 樹的最大直徑 有兩種作法 https://leetcode.cn/problems/diameter-of-binary-tree/
        # 利用輔助遞迴求深度的函數
        # 間接求得 最大直徑

        ans = float('-inf')

        def oneSideMaxSum(root) -> int:
            nonlocal ans

            if root is None:
                return 0

            left = oneSideMaxSum(root.left)
            right = oneSideMaxSum(root.right)

            # 子葉節點為負號的話, 此答案會有問題
            # 因為 0 > 負
            ans = max(ans,
                      left,
                      root.val,
                      right,
                      left + root.val,
                      right + root.val,
                      left + root.val + right)

            return max(left, right) + root.val

        oneSideMaxSum(root)
        return int(ans)

    def maxPathSum_fail(self, root: Optional[TreeNode]) -> int:
        # 由於 左右樹 的節點會互相影響路徑
        # 感覺 前序 後序 都不適合此題目
        # 可能要中序? 從左到右 或 從右到左 的時間點, 進行判斷
        # 此答案嘗試用 後序 解題, 但失敗

        # 前序位置的代码只能从函数参数中获取父节点传递来的数据，
        # 而后序位置的代码不仅可以获取参数数据，还可以 获取到子树的資訊

        if root is None:
            return 0

        left = self.maxPathSum_fail(root.left)
        right = self.maxPathSum_fail(root.right)
        return max(left,
                   root.val,
                   right,
                   left + root.val,
                   right + root.val,
                   left + root.val + right)


if __name__ == '__main__':
    # root1 = create_tree_by_level_order([-10, 9, 20, None, None, 15, 7])
    # root1 = create_tree_by_level_order([-10, 10, 20, 1000, None, 100, 3])
    root1 = create_tree_by_level_order([-3])
    print(Solution().maxPathSum_v1(root1))

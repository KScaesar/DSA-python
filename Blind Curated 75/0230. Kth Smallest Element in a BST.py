from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/kth-smallest-element-in-a-bst/

    def kthSmallest_v2(self, root: Optional[TreeNode], k: int) -> int:
        # 利用 inorder

        rank = 0
        ans = None

        def traversal(root):
            nonlocal rank, ans
            if root is None:
                return

            traversal(root.left)
            rank += 1
            if rank == k:
                ans = root.val
                return
            traversal(root.right)

        traversal(root)
        return ans

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 相似的解題概念
        # 0124. Binary Tree Maximum Path Sum

        rank = self.count(root.left) + 1
        # print(root.val, rank, k)
        if rank == k:
            return root.val
        elif rank > k:
            return self.kthSmallest(root.left, k)
        elif rank < k:
            return self.kthSmallest(root.right, k - rank)

    def count(self, root) -> int:
        if root is None:
            return 0
        left = self.count(root.left)
        right = self.count(root.right)
        return left + right + 1


if __name__ == '__main__':
    root1 = create_tree_by_level_order([3, 1, 4, None, 2, None, None])
    # print(tree.traversal.pre_order_recursive(root1))
    print(Solution().kthSmallest(root1, 1))
    # print(Solution().count(root1.right))

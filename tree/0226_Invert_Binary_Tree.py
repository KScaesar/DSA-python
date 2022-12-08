from typing import Optional

from tool import *
from tree.traversal import pre_order_recursive


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # tree1 = self.invertTree(root.left)
        # tree2 = self.invertTree(root.right)
        # root.right = tree1
        # root.left = tree2

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == '__main__':
    obj = Solution()
    root1 = create_tree_by_level_order([4, 2, 7, 1, 3, 6, 9])
    print(f'{pre_order_recursive(root1)}')

    sol1 = obj.invertTree(root1)
    print(f'{pre_order_recursive(sol1)}')

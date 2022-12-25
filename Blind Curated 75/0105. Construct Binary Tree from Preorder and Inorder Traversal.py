from typing import List, Optional

import tree.traversal
from tool import *


class Solution:
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

    @debug_helper
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        size1 = len(inorder)
        if size1 == 0:
            return None

        root_v = preorder[0]
        pivot = -1
        for i in range(size1):
            if inorder[i] == root_v:
                pivot = i
                break

        left = inorder[:pivot]
        right = inorder[pivot + 1:]

        root = TreeNode(val=root_v)

        # 以 inorder 來看
        # pivot 的解釋, 左子樹 有幾個節點
        #
        # 以 preorder 來看
        # 左子樹的範圍 就是 第一個索引(root) 的 (下一個索引 + 左子樹的節點數量)
        # pivot 相當於長度, [left, right) 左閉右開的長度為 right-left == [left, left+len)
        root.left = self.buildTree(preorder[1:1 + pivot], left)
        root.right = self.buildTree(preorder[pivot + 1:], right)
        return root


if __name__ == '__main__':
    root1 = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(tree.traversal.in_order_iterative_v1(root1))
    print()

    root1 = Solution().buildTree([1, 2], [1, 2])
    print(tree.traversal.in_order_iterative_v1(root1))

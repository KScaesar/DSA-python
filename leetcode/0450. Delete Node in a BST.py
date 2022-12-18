from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/delete-node-in-a-bst/
    def deleteNode_v2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            left = root.left
            right = root.right

            if right is not None:
                # search min value node
                cursor = root.right
                while cursor and cursor.left:  # 父子節點定義方法1
                    cursor = cursor.left

                # 把右節點的最小節點 和 原本的左節點 進行連結
                # 並把右節點變成根節點
                cursor.left = left
                root = right
            else:
                root = left

            return root

        # 利用 bst 的特性
        # 加速找到目標節點
        if root.val > key:
            root.left = self.deleteNode_v2(root.left, key)
        else:
            root.right = self.deleteNode_v2(root.right, key)
        return root

    def deleteNode_v1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            left = root.left
            right = root.right

            if right is not None:
                # search min value node
                parent = root
                cursor = root.right
                while cursor:  # 父子節點定義方法2
                    parent = cursor
                    cursor = cursor.left

                parent.left = left
                root = right
            else:
                root = left

            return root

        # 浪費多餘的時間尋訪
        # 應該利用 bst 的特性
        root.left = self.deleteNode_v1(root.left, key)
        root.right = self.deleteNode_v1(root.right, key)
        return root

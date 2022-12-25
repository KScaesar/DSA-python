from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/validate-binary-search-tree/

    # https://leetcode.com/problems/validate-binary-search-tree/solutions/32112/learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-java-solution/?orderBy=most_votes
    def isValidBST_dfs(self, root: Optional[TreeNode]) -> bool:
        # dfs 尋訪的時候
        # 在參數上 攜帶 必要條件
        # 讓每個節點都必須遵守

        # 左節點使用 _max
        # 右節點使用 _min

        def dfs_v2(root, _min, _max) -> bool:
            # 神奇的想法

            if root is None:
                return True

            if _min >= root.val or root.val >= _max:
                return False

            return dfs_v2(root.left, _min, root.val) and dfs_v2(root.right, root.val, _max)

        def dfs_v1(root, _min, _max) -> bool:
            if root is None:
                return True
            if root.left is None and root.right is None:
                return True

            if root.left and root.right:
                left = root.left.val
                right = root.right.val
                if _min < left < root.val < right < _max:
                    return dfs_v1(root.left, _min, root.val) and dfs_v1(root.right, root.val, _max)
                else:
                    return False

            elif root.left is None and root.right:
                right = root.right.val
                if root.val < right < _max:
                    return dfs_v1(root.left, _min, root.val) and dfs_v1(root.right, root.val, _max)
                else:
                    return False

            if root.left and root.right is None:
                left = root.left.val
                if _min < left < root.val:
                    return dfs_v1(root.left, _min, root.val) and dfs_v1(root.right, root.val, _max)
                else:
                    return False

        return dfs_v2(root, float('-inf'), float('inf'))
        # return dfs_v1(root, float('-inf'), float('inf'))

    def isValidBST_inorder_v3(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        prev = None
        valid = True
        stack = []

        cursor: 'TreeNode' = root
        while True:
            while cursor:
                stack.append(cursor)
                cursor = cursor.left

            cursor = stack.pop()
            if prev is not None:
                if prev >= cursor.val:
                    valid = False
            prev = cursor.val
            cursor = cursor.right

            if len(stack) == 0 and cursor is None or not valid:
                break

        return valid

    def isValidBST_inorder_v2(self, root: Optional[TreeNode]) -> bool:
        # 修改 v1 版本, 優化空間
        # 但發現 遞迴版本 不管如何
        # 空間複雜度都很差, 需要用迭代版本 v3

        # buf = []
        prev = None
        valid = True

        def traversal(root):
            nonlocal valid, prev
            if not valid:
                return

            if root is None:
                return

            traversal(root.left)
            if prev is not None:
                if prev >= root.val:
                    valid = False
            prev = root.val
            traversal(root.right)

        traversal(root)
        return valid

    def isValidBST_inorder_v1(self, root: Optional[TreeNode]) -> bool:
        # 用 inorder 輸出內容
        # 檢查是否有為 遞增數列

        buf = []
        valid = True

        def traversal(root):
            nonlocal valid
            if not valid:
                return

            if root is None:
                return

            # 錯誤的檢查位置
            # if len(buf) != 0:
            #     if buf[-1] >= root.val:
            #         valid = False

            traversal(root.left)
            if len(buf) != 0:
                if buf[-1] >= root.val:
                    valid = False
            buf.append(root.val)
            traversal(root.right)

        traversal(root)
        return valid

        # 容果沒使用 另外的 valid 變數
        # 需要走訪全部節點, 才能知道是否有效
        #
        # for i in range(1, len(buf)):
        #     if buf[i - 1] >= buf[i]:
        #         return False
        # return True

    def isValidBST_fail2(self, root: Optional[TreeNode]) -> bool:
        # 用前序尋訪, 檢查的條件太多了
        # 改用後序尋訪, 發現要檢查的條件差不多
        # 想不到其他方式

        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        # 不忘記要檢查只有單個子葉節點的情境
        if root.left is None or root.right is None:
            left = float('-inf') if root.left is None else root.left.val
            right = float('inf') if root.right is None else root.right.val
            if left >= root.val or root.val >= right:
                return False

        if root.left and root.right:
            if root.left.val < root.val < root.right.val:
                cursor = root.right
                while cursor.left:
                    if root.left.val > cursor.left.val:
                        return False
                    cursor = cursor.left

                cursor = root.left
                while cursor.right:
                    if root.right.val < cursor.right.val:
                        return False
                    cursor = cursor.left
            else:
                return False

        return self.isValidBST_fail2(root.left) and self.isValidBST_fail2(root.right)

    def isValidBST_fail(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left and root.right:
            # 沒有處理 等於 的情況
            if max(root.left.val, root.val, root.right.val) != root.right.val:
                return False
            if min(root.left.val, root.val, root.right.val) != root.left.val:
                return False

            cursor = root.right
            while cursor.left:
                if root.left.val > cursor.left.val:
                    return False
                cursor = cursor.left

        return self.isValidBST_fail(root.left) and self.isValidBST_fail(root.right)


if __name__ == '__main__':
    print(Solution())

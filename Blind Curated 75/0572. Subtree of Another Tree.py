from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/subtree-of-another-tree/
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time complexity: O(|s| * min(|s|, |t|)
        # For every N node in the tree, we check if the tree rooted at node is identical to subRoot
        # This check takes O(M) time, where M is the number of nodes in subRoot

        # Merkle tree
        # 利用 hash 函數, 把整個子樹變成 hash
        # 可以令 時間為 O(M+M)
        # https://leetcode.com/problems/subtree-of-another-tree/solutions/102741/python-straightforward-with-explanation-o-st-and-o-s-t-approaches/

        def traversal(root, subRoot, is_match_at_prev_root) -> bool:
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False

            # 容易誤判的地方
            # 即使根節點不滿足 不應該直接回傳 False
            # 要繼續嘗試, 子節點是否滿足
            # 否則下面的情境會錯誤
            # root = [1,1], subRoot = [1]
            if root.val == subRoot.val:
                if traversal(root.left, subRoot.left, True) and traversal(root.right, subRoot.right, True):
                    return True

            if is_match_at_prev_root:
                return False
            else:
                return traversal(root.left, subRoot, False) or traversal(root.right, subRoot, False)

        return traversal(root, subRoot, False)


if __name__ == '__main__':
    print(Solution())

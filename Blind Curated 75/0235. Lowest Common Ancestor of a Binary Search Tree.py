from tool import *


class Solution:
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

    def lowestCommonAncestor_v4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 利用 bst 特性
        # 使用 v2 的概念, 不需要另外使用 contain_child

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor_v4(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor_v4(root.right, p, q)

        return root

    def lowestCommonAncestor_v3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # postorder
        #
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md
        #
        # 算法筆記 p270

        if root is None:
            return None

        # p q 其中一個 在 root
        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor_v3(root.left, p, q)
        right = self.lowestCommonAncestor_v3(root.right, p, q)

        # p q 分別在 left, right
        if left and right:
            return root

        # p q 集中在 left or right
        elif left or right:
            return left if left else right

        # p or q 不存在 二元樹
        # 題目保證存在, 所以可以不寫此行
        else:
            return None

    def lowestCommonAncestor_v2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # preorder
        # v2 比 v1 好理解
        # 分為四種情況

        left_p = self.contain_child(root.left, p)
        left_q = self.contain_child(root.left, q)
        right_p = self.contain_child(root.right, p)
        right_q = self.contain_child(root.right, q)

        # p q 其中一個 在 root
        if root is p or root is q:
            return root

        # p q 兩個都在 left
        elif left_p and left_q:
            return self.lowestCommonAncestor_v2(root.left, p, q)

        # p q 兩個都在 right
        elif right_p and right_q:
            return self.lowestCommonAncestor_v2(root.right, p, q)

        # p q 分別在 left, right
        else:
            return root

    def lowestCommonAncestor_v1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not self.contain_child(root.left, p) and not self.contain_child(root.left, q):
            if root is p or root is q:
                return root
            else:
                return self.lowestCommonAncestor_v1(root.right, p, q)

        if not self.contain_child(root.right, p) and not self.contain_child(root.right, q):
            if root is p or root is q:
                return root
            else:
                return self.lowestCommonAncestor_v1(root.left, p, q)

        return root

    def contain_child(self, root, child) -> bool:
        if root is None:
            return False
        if root is child:
            return True

        left = self.contain_child(root.left, child)
        right = self.contain_child(root.right, child)
        return left or right


if __name__ == '__main__':
    print(Solution())

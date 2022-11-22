import factory
import traversal
from model import TreeNode


def lca(root, p, q) -> TreeNode | None:
    # 算法筆記 p270
    # lowest common ancestor

    if root is None:
        return None

    # 此 base case 要再想想來由
    # 題目說明 p, q 一定存在
    if root == q or root == p:
        # print(
        #     f'root={(p.value, id(root))}, p={(p.value, id(p))}, q={(q.value, id(q))}')
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left == right is None:
        return None
    elif left is not None and right is not None:
        return root
    elif left is not None and right == None:
        return left
    elif left is None and right is not None:
        return right


if __name__ == '__main__':
    root1 = factory.level_order(
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, None, None, None, None])
    print(traversal.in_order_recursive(root1))

    p = root1.left.left
    q = root1.left.right.left
    print(f'p={(p.value, id(p))}, q={(q.value, id(q))}')
    print(f'lca node = {lca(root1, p, q).value}\n')

    # 如果 p, q 不存在 tree 中
    # 此解法會有錯誤
    # p = root1.left.left
    # q = TreeNode(9)
    # print(f'p={(p.value, id(p))}, q={(q.value, id(q))}')
    # print(f'lca node = {lca(root1,p,q)}\n')

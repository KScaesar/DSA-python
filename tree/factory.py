from model import TreeNode
import traversal


def pre_order(src: list[int | None]) -> 'TreeNode':
    # 算法筆記 p257

    if len(src) == 0:
        return None

    # 重點 先找出 root 位置
    first = src.pop(0)
    if first == None:
        return None

    root = TreeNode(first)
    root.left = pre_order(src)
    root.right = pre_order(src)

    return root


def level_order(src: list[int | None]) -> 'TreeNode':
    # 算法筆記 p264

    if len(src) == 0:
        return None
    if src[0] == None:
        return None

    root = TreeNode(src[0])
    cursor = 1

    queue = [root]

    # print(cursor, [node.value for node in queue])
    while cursor < len(src):
        # print()

        # queue 保存的都是 父節點
        parent = queue.pop(0)

        # 應該 先從 src 取值, curosr 再前進
        # 不應該 先 curosr 前進 , 才從 src 取值
        # 會跳過一個 inden
        left = src[cursor]
        cursor += 1
        if left != None:
            parent.left = TreeNode(left)
            queue.append(parent.left)
        else:
            parent.left = None
        # print(cursor, [node.value for node in queue])

        right = src[cursor]
        cursor += 1
        if right != None:
            parent.right = TreeNode(right)
            queue.append(parent.right)
        else:
            parent.right = None
        # print(cursor, [node.value for node in queue])

        # print(f'left={left} right={right}')

    return root


def is_same_tree(root1: 'TreeNode', root2: 'TreeNode') -> bool:
    if root1 == None and root2 == None:
        return True
    elif (root1 != None and root2 == None) or (root1 == None and root2 != None):
        return False

    if root1.value != root2.value:
        return False

    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)


if __name__ == '__main__':
    root1 = pre_order([1, 2, None, 4, None, None, 3, None, None])
    print(f'root1={traversal.pre_order_recursive(root1)}\n')

    # root2 = level_order([1, 2, 3, None, 4, None, None, None, None])
    root2 = level_order([1, 2, 3, None, None, 4, None, None, None])
    print(f'root2={traversal.pre_order_recursive(root2)}\n')

    print(f'root1 and root2 is same tree? {is_same_tree(root1,root2)}\n')

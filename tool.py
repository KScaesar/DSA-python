from dataclasses import dataclass


def debug_helper(func):
    cnt = 0
    symbol = '| '

    def wrapper(*args, **kwargs):
        nonlocal cnt
        indent = symbol * cnt
        print(f'{indent}-> {args} {kwargs if kwargs else ""}')

        cnt += 1
        res = func(*args, **kwargs, indent=indent + "->")
        cnt -= 1

        print(f'{symbol * cnt}<- {args} {kwargs if kwargs else ""}, return={res if res else ""}')
        return res

    return wrapper


@dataclass
class ListNode:
    val: int | None
    previous: 'ListNode' = None
    next: 'ListNode' = None

    def __str__(self):
        return str(self.val)


def traversal_linklist(head: 'ListNode') -> list[int]:
    result = []

    if head == None:
        return result

    cursor: 'ListNode' = head
    while cursor:
        result.append(cursor.val)
        # result.append((id(cursor), cursor.value))
        cursor = cursor.next

    return result


def create_linklist_from_array(nums: list[int]) -> (ListNode, ListNode):
    dummy = ListNode(None)

    cursor = dummy
    for v in nums:
        cursor.next = ListNode(v)
        cursor = cursor.next
    tail = cursor

    head = dummy.next
    dummy.next = None
    return head, tail


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None
    isVisited: bool = False

    def __str__(self):
        return str(self.val)


def create_tree_by_pre_order(src: list[int | None]) -> TreeNode | None:
    # 算法筆記 p257

    if len(src) == 0:
        return None

    # 重點 先找出 root 位置
    first = src.pop(0)
    if first == None:
        return None

    root = TreeNode(first)
    root.left = create_tree_by_pre_order(src)
    root.right = create_tree_by_pre_order(src)

    return root


def create_tree_by_level_order(src: list[int | None]) -> TreeNode | None:
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

    if root1.val != root2.val:
        return False

    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)


def print_matrix(grid: list[list[any]], **info):
    m = len(grid)
    n = len(grid[0])

    other = {k: v for k, v in info.items() if k != "indent"}
    indent = info.get("indent", "")
    targets = info.get('targets', [])
    print(f'{indent} m={m} n={n} {other}')

    for row in range(m):
        print(f'{indent}', end="")
        for col in range(n):
            element = grid[row][col] if grid[row][col] is not None else '_'
            if (row, col) in targets:
                element = "*" + str(element)
                print(f'{element:>{5}}', end="")
            else:
                print(f'{element:>{5}}', end="")
        print()
    print(indent)


if __name__ == '__main__':
    root1 = create_tree_by_pre_order([1, 2, None, 4, None, None, 3, None, None])

    # root2 = create_tree_by_level_order([1, 2, 3, None, 4, None, None, None, None])
    root2 = create_tree_by_level_order([1, 2, 3, None, None, 4, None, None, None])

    print(f'root1 and root2 is same tree? {is_same_tree(root1, root2)}\n')

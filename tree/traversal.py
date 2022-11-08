from model import TreeNode


def pre_order_recursive(root: 'TreeNode') -> list[int]:
    result = []

    def helper(root: 'TreeNode'):
        nonlocal result
        if root == None:
            return

        result.append(root.value)
        helper(root.left)
        helper(root.right)

    helper(root)
    return result


def in_order_recursive(root: 'TreeNode') -> list[int]:
    result = []

    def helper(root: 'TreeNode'):
        nonlocal result
        if root == None:
            return

        helper(root.left)
        result.append(root.value)
        helper(root.right)

    helper(root)
    return result


def post_order_recursive(root: 'TreeNode') -> list[int]:
    result = []

    def helper(root: 'TreeNode'):
        nonlocal result
        if root == None:
            return

        helper(root.left)
        helper(root.right)
        result.append(root.value)

    helper(root)
    return result


def create_example_tree() -> 'TreeNode':
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n2 = TreeNode(2, n1, n3)
    n6 = TreeNode(6, n5, n7)
    n4 = TreeNode(4, n2, n6)
    return n4


def main():
    # https://shubo.io/iterative-binary-tree-traversal
    root = create_example_tree()

    print(pre_order_recursive(root), "pre_order recursive")
    print()

    print(in_order_recursive(root), "in_order recursive")
    print()

    print(post_order_recursive(root), "post_order recursive")
    print()


if __name__ == '__main__':
    # import sys
    # print(sys.path)

    main()

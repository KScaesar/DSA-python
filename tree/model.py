from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None
    isVisited: bool = False

def create_example_tree() -> 'TreeNode':
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n2 = TreeNode(2, n1, n3)
    n6 = TreeNode(6, n5, n7)
    n4 = TreeNode(4, n2, n6)
    return n4
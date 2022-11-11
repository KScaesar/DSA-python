from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None
    isVisited: bool = False

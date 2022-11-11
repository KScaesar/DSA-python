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


def pre_order_iterative_v1(root: 'TreeNode') -> list[int]:
    if root == None:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.append(current.value)

        # https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
        #
        # 雖然 preorder 輸出是先左再右
        # 但因為 stack 的特性是 先進後出
        # 所以利用 stack 結構的時候
        # 需要先把右節點放入 stack
        # pop 才會讓 右節點, 比較晚出現
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

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


def in_order_iterative_v1(root: 'TreeNode') -> list[int]:
    if root == None:
        return []

    result = []
    stack = []

    current: 'TreeNode' = root
    while True:

        # 不需要另外定義 TreeNode.isVisited
        # 因為 stack.append(node) 同等意義 node.isVisited = True
        #
        # while current and not current.isVisited:
        #     current.isVisited = True
        #     stack.append(current)
        #     current = current.left

        # v2 方法更直覺, 每次只判斷一個階層的節點
        # v1 則是先一路走完左節點
        while current:
            stack.append(current)
            current = current.left

        # print("stack =", [x.value for x in stack])
        # print("result =", result)
        current = stack.pop()
        result.append(current.value)
        current = current.right

        if len(stack) == 0 and current == None:
            break

    return result


def in_order_iterative_v2(root: 'TreeNode') -> list[int]:
    if root == None:
        return []

    result = []
    stack = []

    current: 'TreeNode' = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()

            result.append(current.value)
            current = current.right

        if len(stack) == 0 and current == None:
            break

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


def post_order_iterative_v1_fail(root: 'TreeNode') -> list[int]:
    if root == None:
        return []

    result = []
    stack = []

    current: 'TreeNode' = root
    isBacktrace = False
    while True:
        if current and not isBacktrace:
            stack.append(current)
            if current.right:
                stack.append(current.right)  # 測試後才發現, 不應該先放入右節點
            current = current.left
        else:
            current = stack.pop()
            isBacktrace = True
            result.append(current.value)

        print("stack =", [x.value for x in stack])
        print("result =", result)
        # success result = [1, 3, 2, 5, 7, 6, 4]
        #
        # but this function fail
        # fail result = [1, 3, 2, 6, 4]
        #
        #     current = stack.pop()
        # IndexError: pop from empty list

        if len(stack) == 0 and current == None:
            break

    return result


def post_order_iterative_v1(root: 'TreeNode') -> list[int]:
    if root == None:
        return []

    result = []
    stack = []

    node = root
    isBacktrace = False
    while len(stack) != 0 or not isBacktrace:  # 中止條件 經由多次測試嘗試才得知, 面試需求可能要死記
        if node and not isBacktrace:
            stack.append({'node': node, 'isBacktrace': False})
            node = node.left
        else:
            current = stack[-1]
            if not current['isBacktrace']:
                current['isBacktrace'] = True
                node = current['node'].right
                isBacktrace = False
            else:
                result.append(current['node'].value)
                current = stack.pop()
                node = current['node']
                isBacktrace = current['isBacktrace']

        # print("stack =", [(x['node'].value, x['isBacktrace']) for x in stack])
        # print("result =", result, "\n")

    return result


def post_order_iterative_v2(root: 'TreeNode') -> list[int]:
    '''
    參考網路解答得來的
    對我而言是很特別的思考方式

    將父節點和左右子節點都放進 stack 中，並將父節點的左右子節點設為 NULL。
    當 stack pop 出一個節點沒有左右子節點時，表示他的左右子節點已經被拜訪過了，則可以拜訪父節點。

    Postorder 的原則是
    當目前節點的兩個子節點都確認過以後, 才會讀取目前的節點

    https://shubo.io/iterative-binary-tree-traversal/
    '''

    if root == None:
        return []

    result = []
    stack = [root]

    while len(stack) != 0:
        current = stack[-1]

        if current.left == None and current.right == None:
            result.append(current.value)
            current = stack.pop()

        if current.right:
            stack.append(current.right)
            current.right = None

        if current.left:
            stack.append(current.left)
            current.left = None

        # print("stack =", [x.value for x in stack])
        # print("result =", result, "\n")

    return result


def post_order_iterative_v3(root: 'TreeNode') -> list[int]:
    '''
    參考網路解答得來的
    對我而言是很特別的思考方式

    拿到的root,本身就是後序走訪中的最後一個,我們剛好可以利用這一點,反過來輸出答案。
    每一次我們到的新Node,把它之下的整個結構,想像成是一棵小一點的二元樹
    這樣那顆新的Node就變成另一個root
    那新的Node就都是最後一個讀取的,所以就把它加到最前面,再往下找其他Nodo

    https://ithelp.ithome.com.tw/articles/10247992
    '''

    if root == None:
        return []

    result = []
    stack = [root]

    while len(stack) != 0:
        current = stack.pop()
        if current != None:
            result.insert(0, current.value)

        # 注意 此方法是先 push 左節點 到 stack
        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

        # print("stack =", [x.value for x in stack])
        # print("result =", result, "\n")

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

    # 想清楚 iterative 的 子葉中止條件是什麼
    # current_node == None
    #
    # 需要特別死記 遞迴形式的外部大迴圈中止條件
    # 不同尋訪方式 中止條件不一樣
    #
    # 一開始可以不用先思考 外部迴圈的中止條件
    # 先撰寫尋訪過程的程式碼

    print(pre_order_recursive(create_example_tree()),
          pre_order_recursive.__name__)
    print(pre_order_iterative_v1(create_example_tree()),
          pre_order_iterative_v1.__name__)
    print()

    print(in_order_recursive(create_example_tree()), in_order_recursive.__name__)
    print(in_order_iterative_v1(create_example_tree()),
          in_order_iterative_v1.__name__)
    print(in_order_iterative_v2(create_example_tree()),
          in_order_iterative_v2.__name__)
    print()

    print(post_order_recursive(create_example_tree()),
          post_order_recursive.__name__)
    print(post_order_iterative_v1(create_example_tree()),
          post_order_iterative_v1.__name__)
    print(post_order_iterative_v2(create_example_tree()),
          post_order_iterative_v2.__name__)
    print(post_order_iterative_v3(create_example_tree()),
          post_order_iterative_v3.__name__)
    print()

    # print(post_order_iterative_v1_fail(create_example_tree()),
    #       post_order_iterative_v1_fail.__name__)


if __name__ == '__main__':
    # import sys
    # print(sys.path)

    main()

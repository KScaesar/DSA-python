from model import traversal_linklist


def debugHelper(func):
    cnt = 0
    indent = '| '

    def wrapper(*args, **kwargs):
        nonlocal cnt
        # print(f'{indent*cnt}-> {args}')
        print(f'{indent*cnt}-> {traversal_linklist(args[0])}')

        cnt += 1
        res = func(*args, **kwargs)
        cnt -= 1

        # print(f'{indent*cnt}<- {args}, result={res}')
        print(f'{indent*cnt}<- result={res}')
        return res
    return wrapper
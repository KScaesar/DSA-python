def debugHelper(func):
    cnt = 0
    indent = '│ '

    def wrapper(*args, **kwargs):
        nonlocal cnt
        print(f'{indent*cnt}-> {args}')

        cnt += 1
        res = func(*args, **kwargs)
        cnt -= 1

        print(f'{indent*cnt}<- {args}, result={res}')
        return res
    return wrapper
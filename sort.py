# sort
# https://officeguide.cc/python-sort-sorted-tutorial-examples/
#
# multi condition -> lamdba return tuple
# https://blog.csdn.net/y12345678904/article/details/77507552

data = [(1, 2), (7, 1), (3, 6), (4, 5), (2, 9)]

data.sort(key=lambda k: (k[0]*k[1], -k[0]))
print(data)

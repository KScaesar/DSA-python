from typing import List


class Solution:
    # https://leetcode.com/problems/destination-city/description/

    def destCity(self, paths: List[List[str]]) -> str:
        _graph = dict()
        for path in paths:
            _from, _to = path
            if _from not in _graph:
                _graph[_from] = [_to]
            else:
                _graph[_from].append(_to)

        _from_list = _graph.keys()
        for path in paths:
            _, _to = path
            if _to not in _from_list:
                return _to


if __name__ == '__main__':
    print(Solution())
